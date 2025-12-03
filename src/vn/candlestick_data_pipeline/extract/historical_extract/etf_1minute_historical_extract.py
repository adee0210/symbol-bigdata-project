from utils.load_file_to_variable_util import LoadFileToVariableUtil
from utils.selenium_util import SeleniumUtil


class ETF1MinuteHistoricalExtract:
    def __init__(self):
        self.vn_candlestick_data = LoadFileToVariableUtil.load_json_to_variable(
            "symbol_bigdata_project_config.json", "vn_candlestick_data"
        )

        self.etf_data_source_url = self.vn_candlestick_data["data_source_url"]
        self.etf_symbol_list = self.vn_candlestick_data["symbols"]["etf"]

    def extract_logic(self):
        now
