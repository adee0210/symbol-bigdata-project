import json
import os
import sys
import requests

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
from src.utils.get_path_util import GetPathUtil
from configs.logger_config import LoggerConfig
from configs.variable_config import CMC_CONFIG


class CMCTop100WithIdSymbolExtract:

    def __init__(self) -> None:
        try:
            self.logger = LoggerConfig.logger_config("Top100 symbol with id extract")
            self.cmc_key = CMC_CONFIG["cmc_realtime_key"]
            self.cmc_url = CMC_CONFIG["cmc_realtime_url"]
            self.headers = self.header = {
                "Accept": "application/json",
                "X-CMC_PRO_API_KEY": self.cmc_key,
            }
            self.logger.info("Loaded CMC data configuration successfully")
        except Exception as e:
            self.logger.error(
                f"Can not load CMC data configuration with Error: {str(e)}"
            )

    def extract(self):

        try:
            self.logger.info("Starting to extract CMC top100 symbol with id data ...")
            response_data = requests.get(
                url=self.cmc_url, headers=self.headers, timeout=30
            ).json()

            if (
                response_data.get("status").get("error_code") == 0
                and response_data.get("status").get("error_message") is None
            ):

                symbol_top100 = response_data["data"]

                self.logger.info("Successfully to extract CMC top100 symbol data.")
                symbol_top100_with_id_list = [
                    {"id": data["id"], "name": data["name"], "symbol": data["symbol"]}
                    for data in symbol_top100
                ]
                file_path = os.path.join(
                    GetPathUtil.get_data_raw_path(), "top100_symbol_with_id.json"
                )
                with open(file_path, "w") as f:
                    json.dump(symbol_top100_with_id_list, f)

                return symbol_top100_with_id_list

            else:
                self.logger.error(
                    f"Can not extract top100 symbol data: {response_data.get("status").get("error_message")}"
                )
                return None

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Requests error: {str(e)}")
            return None

        except Exception as e:
            self.logger.error(f"Unexpected error in cmc_extract: {str(e)}")
            return None
