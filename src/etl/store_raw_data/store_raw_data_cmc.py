from configs.logger_config import LoggerConfig
from configs.postgresql_config import AsyncPGConfig


class StoreRawDataCMC:
    def __init__(self) -> None:
        self.logger = LoggerConfig.logger_config(
            "Store raw extract historical data from CMC extract data"
        )
        self.async_pg_config = AsyncPGConfig()
        self.get_pool = None

    async def init_pool(self):
        self.pool = await self.async_pg_config.get_pool()
