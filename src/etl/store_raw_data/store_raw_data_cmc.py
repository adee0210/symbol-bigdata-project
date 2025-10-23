from configs.logger_config import LoggerConfig
from configs.postgresql_config import AsyncPGConfig
from configs.variable_config import CMC_CONFIG


class StoreRawDataCMC:
    def __init__(self) -> None:
        self.logger = LoggerConfig.logger_config(
            "Store raw extract historical data from CMC extract data"
        )
        self.async_pg_config = AsyncPGConfig()
        self.cmc_table_in_pg = CMC_CONFIG["cmc_table_in_pg"]

    async def update_cmc_symbol(self):
        pool = await self.async_pg_config.get_pool()
        async with pool.acquire() as conn:
            async with conn.transaction():
                r = conn.execute(
                    f"""
                    UPDATE {self.cmc_table_in_pg}
                    SET name = $1
                    """
                )
