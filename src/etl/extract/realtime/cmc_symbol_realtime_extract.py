import sys
import os

from utils.convert_datetime_util import ConvertDatetimeUtil

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
import json
import requests
from configs.logger_config import LoggerConfig
from configs.variable_config import CMC_CONFIG


class CMCRealtimeExtract:
    def __init__(self) -> None:
        try:
            self.logger = LoggerConfig.logger_config(
                "Extract CMC realtime data from CMC API"
            )
            self.cmc_key = CMC_CONFIG["cmc_key"]
            self.cmc_url = CMC_CONFIG["cmc_url"]
            self.cmc_interval_send_request = CMC_CONFIG["cmc_interval_send_request"]
            self.headers = self.header = {
                "Accept": "application/json",
                "X-CMC_PRO_API_KEY": self.cmc_key,
            }
            self.cmc_top100_symbol_name = CMC_CONFIG["cmc_top100_symbol_name"]
            self.logger.info("Loaded CMC realtime data configuration successfully")
        except Exception as e:
            self.logger.error(
                f"Can not load CMC realtime data configuration with Error: {str(e)}"
            )

    def extract(self):
        try:
            self.logger.info("Starting to extract CMC realtime data ...")
            response_data = requests.get(
                url=self.cmc_url, headers=self.headers, timeout=30
            ).json()

            if (
                response_data.get("status").get("error_code") == 0
                and response_data.get("status").get("error_message") is None
            ):
                list_data = response_data["data"]
                realtime_data_extract = [
                    {
                        "name": data["name"],
                        "symbol": data["symbol"],
                        "rank": data["cmc_rank"],
                        "circulating_supply": data["circulating_supply"],
                        "total_supply": data["total_supply"],
                        "price": data["quote"]["USD"]["price"],
                        "percent_change_1h": data["quote"]["USD"]["percent_change_1h"],
                        "percent_change_24h": data["quote"]["USD"][
                            "percent_change_24h"
                        ],
                        "percent_change_7d": data["quote"]["USD"]["percent_change_7d"],
                        "percent_change_30d": data["quote"]["USD"][
                            "percent_change_30d"
                        ],
                        "percent_change_60d": data["quote"]["USD"][
                            "percent_change_60d"
                        ],
                        "percent_change_90d": data["quote"]["USD"][
                            "percent_change_90d"
                        ],
                        "market_cap": data["quote"]["USD"]["market_cap"],
                        "market_cap_dominance": data["quote"]["USD"][
                            "market_cap_dominance"
                        ],
                        "datetime": ConvertDatetimeUtil.isoformat_datetime_to_datetime(
                            data["quote"]["USD"]["last_updated"]
                        ),
                    }
                    for data in list_data
                ]
                self.logger.info("Successfully to extract CMC realtime data.")
                top_100_symbol_name_list = [
                    data["symbol"] for data in realtime_data_extract
                ]
                base_dir = os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                        )
                    )
                )
                top100_symbol_full_path = os.path.join(
                    f"{base_dir}/data/raw/", self.cmc_top100_symbol_name
                )
                with open(top100_symbol_full_path, "w") as f:
                    f.write(str(top_100_symbol_name_list))
                self.logger.info(
                    f"Write top 100 symbol name to {top100_symbol_full_path}"
                )

                return realtime_data_extract
            else:
                self.logger.error(
                    f"Can not extract realtime data: {response_data.get("status").get("error_message")}"
                )
                return None

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Requests error: {str(e)}")
            return None

        except Exception as e:
            self.logger.error(f"Unexpected error in cmc_extract: {str(e)}")
            return None
