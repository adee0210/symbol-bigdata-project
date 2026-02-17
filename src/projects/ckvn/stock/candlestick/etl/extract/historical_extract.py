from datetime import datetime, timezone
from logging import Logger
import cloudscraper
from ckvn.stock.candlestick.configs.config import SYMBOL
from ckvn.stock.candlestick.etl.extract.historical_extract_interface import (
    HistoricalExtractInterface,
)

from common.configs.logging_config import LoggingConfig


class HistoricalExtract(HistoricalExtractInterface):
    def __init__(self) -> None:
        self.logger = LoggingConfig.logging_config("HistoricalStockCandlestickExtract")
        self.investing_api = str(SYMBOL["investing_api"])
        self.symbol = [SYMBOL[s].keys() for s in SYMBOL.keys()]

    def logic(self):
        try:
            start_time = int(datetime.now(tz=timezone.utc).timestamp())
            scraper = cloudscraper.create_scraper()
            response = scraper.get(url=self.investing_api)
            data = response.json()
            return data

        except Exception as e:
            self.logger.info(f"Error: {str(e)}")
            raise

    def historical_extract_logic(self):
        return None

    def historical_extract(self):
        return None
