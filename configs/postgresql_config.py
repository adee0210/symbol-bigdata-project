from psycopg_pool import ConnectionPool


class PostgreSQLConfig:
    _instances = {}

    def __new__(cls, base_url, db_name, min_connect=5, max_connect=20):
        if db_name in cls._instances:
            return cls._instances[db_name]
        if base_url is None or db_name is None:
            raise ValueError("Base URL or DB name is None")
        instance = super().__new__(cls)
        full_url = base_url + "/" + db_name
        instance._pool = ConnectionPool(
            full_url, min_size=min_connect, max_size=max_connect
        )
        cls._instances[db_name] = instance
        return instance
