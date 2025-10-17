import asyncpg
from configs.variable_config import POSTGRES_CONFIG


class AsyncPGConfig:
    _instance = None

    def _init_config(self):
        self._config = {
            "host": POSTGRES_CONFIG.get("host", "localhost"),
            "port": int(POSTGRES_CONFIG.get("port", 5432)),
            "user": POSTGRES_CONFIG.get("user", "postgres"),
            "password": POSTGRES_CONFIG.get("password", ""),
            "database": POSTGRES_CONFIG.get("database", "postgres"),
            "min_size": int(POSTGRES_CONFIG.get("min_size", 5)),
            "max_size": int(POSTGRES_CONFIG.get("max_size", 20)),
        }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AsyncPGConfig, cls).__new__(cls)
            cls._instance._init_config()
            cls._instance._pool = None
        return cls._instance

    async def get_pool(self):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(**self._config)
        return self._pool
