from datetime import time, timedelta
import json
from configs.config_env import VN_CANDLESTICK_DATA_CONFIG
from utils.convert_to_format_datetime_util import ConvertToFormatDatetimeUtil
from utils.load_file_to_variable_util import LoadFileToVariableUtil
from utils.selenium_util import SeleniumUtil


class ETF1MinuteHistoricalExtract:
    def __init__(self):
        self.vn_candlestick_data = LoadFileToVariableUtil.load_json_to_variable(
            "symbol_config.json", "vn_candlestick_data"
        )

        self.etf_data_source_url = VN_CANDLESTICK_DATA_CONFIG[
            "vn_candlestick_datasource_url"
        ]
        self.etf_symbol_list = self.vn_candlestick_data["symbols"]["etf"][0]
        self.selenium_util = SeleniumUtil()

    def extract_logic(self):
        time_end = int(time.time())
        stack = 6 * 30 * 24 * 60 * 60

        time_start = time_end - stack
        etf_url = (
            self.etf_data_source_url.replace("symbol", self.etf_symbol_list)
            .replace("time_start", time_start)
            .replace("time_end", time_end)
        )

        while True:
            if (
                self.selenium_util.get_data_by_tag_name(etf_url, "body")["s"]
                == "no_data"
            ):
                break
            time_end = time_start
            time_start = time_end - stack
            etf_url = (
                self.etf_data_source_url.replace("symbol", self.etf_symbol_list)
                .replace("time_start", time_start)
                .replace("time_end", time_end)
            )
            data = self.selenium_util.get_data_by_tag_name(etf_url, "body")
            with open(
                f"/home/duc/symbol-bigdata-project/data/{ConvertToFormatDatetimeUtil.unix_second_to_datetime(time_end)}.json",
                "w",
            ) as f:
                json.dump(data, f)
