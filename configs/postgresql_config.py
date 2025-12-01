from psycopg_pool import ConnectionPool


class PostgreSQLConfig:
    _instance = None

    def __new__(cls, postgresql_db_urls, min_connect=5, max_connect=20):
        if cls._instance is None:
            if postgresql_db_urls is None:
                raise ValueError("PostgreSQL DB is None")
            cls._instance = super().__new__(cls)
            cls._instance_pool = {
                name: ConnectionPool(url, min_size=min_connect, max_size=max_connect)
                for name, url in postgresql_db_urls.items()
            }
            return cls._instance


