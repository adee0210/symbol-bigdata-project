from datetime import datetime, timezone
import json
from logging import Logger
from time import sleep
from ckvn.stock.candlestick.configs.config import SYMBOL, SYMBOL_API
from ckvn.stock.candlestick.etl.extract.historical.historical_extract_interface import (
    HistoricalExtractInterface,
)

from common.configs.logging_config import LoggingConfig
from common.utils.selenium_util import SeleniumUtil


class HistoricalExtract(HistoricalExtractInterface):
    def __init__(self) -> None:
        # self.logger = LoggingConfig.logging_config("HistoricalStockCandlestickExtract",)
        self.investing_api = str(SYMBOL_API["investing_api"])
        self.selenium_util = SeleniumUtil()
        self.symbol = [SYMBOL[s].keys() for s in SYMBOL.keys()]

    def historical_extract(self):
        url = "https://tvc4.investing.com/4379fbb3b2cf9327a768dbfde5d69d1d/1761556750/52/52/110/history?symbol=vcb&resolution=1&from=1738256400&to=1767114000"
        self.selenium_util.extract_element_from_url_to_json(
            url, by_element="tag name", element_name="body"
        )

    def storage_historical_extract_data(self):
        return None


test = HistoricalExtract()
test.historical_extract()
# test.historical_extract_logic()
# end_time = datetime(year=2025, month=12, day=31).timestamp()
# start_time = datetime(year=2025, month=1, day=31).timestamp()
# print(end_time, start_time)
