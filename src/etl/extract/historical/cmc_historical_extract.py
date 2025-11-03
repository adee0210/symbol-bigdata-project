import requests
from configs.logger_config import LoggerConfig
from configs.variable_config import CMC_CONFIG
from utils.convert_datetime_util import ConvertDatetimeUtil


class CMCHistoricalExtract:
    def __init__(self) -> None:
        self.logger = LoggerConfig.logger_config("CMCHistoricalExtract")
        self.cmc_historical_url = CMC_CONFIG["cmc_historical_url"]
        self.cmc_historical_time_end = CMC_CONFIG["cmc_historical_time_end"]
        self.cmc_historical_day = CMC_CONFIG["cmc_historical_day"]
        self.cmc_symbol_id = "1027"

    def get_data_from_requests(self, time_start, time_end):
        try:
            self.logger.info(
                f"Send requests to {self.cmc_historical_url} with timeStart:{ConvertDatetimeUtil.unix_second_to_datetime(time_start)} and timeEnd: {ConvertDatetimeUtil.unix_second_to_datetime(time_end)}"
            )
            response = requests.get(
                url=self.cmc_historical_url.replace(
                    "symbol_id", str(self.cmc_symbol_id)
                )
                .replace("symbol_time_start", str(time_start))
                .replace("symbol_time_end", str(time_end)),
                timeout=30,
            )
            data = response.json()["data"]["quotes"]
            return data

        except Exception as e:
            self.logger.error(f"Error to send request: {(str(e))}")
            return None
