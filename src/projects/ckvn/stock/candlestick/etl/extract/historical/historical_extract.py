from datetime import datetime, timezone
from logging import Logger
import cloudscraper
from ckvn.stock.candlestick.configs.config import SYMBOL
from ckvn.stock.candlestick.etl.extract.historical.historical_extract_interface import (
    HistoricalExtractInterface,
)

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.options import Options

from common.configs.logging_config import LoggingConfig


class HistoricalExtract(HistoricalExtractInterface):
    def __init__(self) -> None:
        self.logger = LoggingConfig.logging_config("HistoricalStockCandlestickExtract")
        self.investing_api = str(SYMBOL["investing_api"])
        self.symbol = [SYMBOL[s].keys() for s in SYMBOL.keys()]

    def logic(self):
        def create_chromium_driver():

        driver_path = r"/snap/bin/chromium.chromedriver"
        chromium_option = Options()
        chromium_option.add_argument("--no-sandbox")
        chromium_option.add_argument("--disable-dev-shm-usage")
        chromium_option.add_argument("--disable-gpu")
        chromium_option.add_argument("--disable-blink-features=AutomationControlled")
        chromium_option.add_argument("--no-first-run")
        chromium_option.add_argument("--disable-default-apps")
        chromium_option.add_argument("--disable-extensions")
        # chromium_option.add_argument("--headless=new")  # Disabled to show browser UI
        return webdriver.Chrome(
            service=ChromiumService(driver_path), options=chromium_option
        )

            


    def historical_extract_logic(self):
        return None

    def historical_extract(self):
        return None
