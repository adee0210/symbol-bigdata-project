import asyncpg
from configs.logger_config import LoggerConfig
from configs.postgresql_config import AsyncPGConfig
from configs.variable_config import CMC_CONFIG


class DatabaseManager:
    def __init__(self):
        self.logger = LoggerConfig.logger_config("DatabaseManager")
        self.pg_config = AsyncPGConfig()
        self.conn = None

    async def connect(self, database: str | None = None):
        try:
            target_db = database or self.pg_config._config.get("database")

            if self.conn is not None and not self.conn.is_closed():
                self.logger.info("Reusing existing PostgreSQL connection")
                return self.conn

            self.conn = await asyncpg.connect(
                user=self.pg_config._config["user"],
                password=self.pg_config._config["password"],
                host=self.pg_config._config["host"],
                port=self.pg_config._config["port"],
                database=target_db,
            )
            self.logger.info(f"Connected to PostgreSQL database: {target_db}")
            return self.conn

        except Exception as e:
            self.logger.error(f"Failed to connect to PostgreSQL: {str(e)}")
            self.conn = None
            raise

    async def close(self):
        try:
            if self.conn is not None and not self.conn.is_closed():
                await self.conn.close()
                self.logger.info("PostgreSQL connection closed")
            self.conn = None
        except Exception as e:
            self.logger.error(f"Error while closing PostgreSQL connection: {str(e)}")

    async def create_database(self):
        """Create database defined in config if it doesn't exist."""
        try:
            database_name = self.pg_config._config.get("database")
            # connect to default 'postgres' to manage databases
            conn = await self.connect(database="postgres")
            if conn is None:
                self.logger.error(
                    "Cannot connect to PostgreSQL server to create database"
                )
                return None

            exists = await conn.fetchval(
                "SELECT 1 FROM pg_database WHERE datname=$1", database_name
            )

            if not exists:
                await conn.execute(f"CREATE DATABASE {database_name}")
                self.logger.info(f"Database created: {database_name}")
            else:
                self.logger.info(f"Database already exists: {database_name}")

        except Exception as e:
            self.logger.error(f"Failed to create database {database_name}: {str(e)}")
            raise
        finally:
            # close admin connection but keep module-level persistent conn None
            try:
                if conn and not conn.is_closed():
                    await conn.close()
                    self.logger.info(
                        "Admin connection closed after database creation check"
                    )
            except Exception:
                pass

    async def create_cmc_table(self):
        table_name = CMC_CONFIG.get("cmc_table_in_pg")
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            name TEXT,
            symbol TEXT,
            rank INTEGER,
            circulating_supply DOUBLE PRECISION,
            total_supply DOUBLE PRECISION,
            price DOUBLE PRECISION,
            percent_change_1h DOUBLE PRECISION,
            percent_change_24h DOUBLE PRECISION,
            percent_change_7d DOUBLE PRECISION,
            percent_change_30d DOUBLE PRECISION,
            percent_change_60d DOUBLE PRECISION,
            percent_change_90d DOUBLE PRECISION,
            market_cap DOUBLE PRECISION,
            market_cap_dominance DOUBLE PRECISION,
            datetime TIMESTAMP
        );
        """

        try:
            conn = await self.connect()
            if conn is None:
                self.logger.error("Cannot connect to database to create CMC table")
                return None

            await conn.execute(create_table_sql)
            self.logger.info(f"Table ensured: {table_name}")

        except Exception as e:
            self.logger.error(f"Failed to create table {table_name}: {str(e)}")
            raise
