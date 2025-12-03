from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from utils.load_file_to_variable_util import LoadFileToVariableUtil


class ETF1MinuteHistoricalExtract:
    def __init__(self):
        self.vn_candlestick_data = LoadFileToVariableUtil.load_json_to_variable(
            "symbol_bigdata_project_config.json", "vn_candlestick_data"
        )

        self.etf_data_source_url = self.vn_candlestick_data["data_source_url"]
        self.etf_symbol_list = self.vn_candlestick_data["symbols"]["etf"]

    def test_selenium(self):
        common_option = [
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-blink-features=AutomationControlled",
            "--no-first-run",
            "--disable-default-apps",
            "--disable-extensions",
            "--headless",
        ]
        chrome_option = Options()
        for option in common_option:
            chrome_option.add_argument(option)

        chrome_service = Service("/usr/bin/chromedriver")
        chrome_driver = webdriver.Chrome(options=chrome_option, service=chrome_service)
