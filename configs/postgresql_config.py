import asyncpg
from configs.variable_config import POSTGRES_CONFIG
from configs.logger_config import LoggerConfig


class AsyncPGConfig:
    _instance = None
    _logger = LoggerConfig.logger_config("AsyncPGConfig")

    def _init_config(self):
        try:
            self._config = {
                "host": POSTGRES_CONFIG.get("host", "localhost"),
                "port": int(POSTGRES_CONFIG.get("port", 5432)),
                "user": POSTGRES_CONFIG.get("user", "postgres"),
                "password": POSTGRES_CONFIG.get("password", ""),
                "database": POSTGRES_CONFIG.get("database", "postgres"),
                "min_size": int(POSTGRES_CONFIG.get("min_size", 5)),
                "max_size": int(POSTGRES_CONFIG.get("max_size", 20)),
            }
        except Exception as e:
            self._logger.error(f"Failed to initialize PostgreSQL config: {str(e)}")

    def __new__(cls):
        try:
            if cls._instance is None:
                cls._instance = super(AsyncPGConfig, cls).__new__(cls)
                cls._instance._init_config()
                cls._instance._pool = None
            return cls._instance
        except Exception as e:
            cls._logger.error(f"Failed to create AsyncPGConfig instance: {str(e)}")
            raise

    async def get_pool(self):
        try:
            if self._pool is None:
                self._pool = await asyncpg.create_pool(**self._config)
            return self._pool
        except Exception as e:
            self._logger.error(f"Failed to get PostgreSQL connection pool: {str(e)}")
            raise
