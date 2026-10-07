import os
import time

from dotenv import load_dotenv

from common.exception.exception_extraction import ExtractionException
from common.exception.exception_validation import ValidationException
from common.utils.util_convert_datetime import ConvertDatetimeUtil
from common.utils.util_fetch_by_curl_util import FetchByCurlUtil

load_dotenv()


class ExtractStockCandlestick:
    def __init__(self, symbol, resolution: str, extract_method: str):
        self.symbol = symbol

        self.convert_datetime_util = ConvertDatetimeUtil()
        self.resolution = self.convert_datetime_util.convert_resolution(resolution)
        self.extract_method = extract_method
        self.url = os.getenv("VPS_URL")

        self.fetch_by_curl_util = FetchByCurlUtil()
        self.extraction_exception = ExtractionException("Extraction error")
        self.validation_exception = ValidationException("Validation error")

    def extract_all_history_data(self):
        if self.extract_method == "curl":
            params = {
                "symbol": self.symbol,
                "resolution": self.resolution,
                "from": int(time.time()) - 10 * 365 * 24 * 60 * 60,  # 10 years ago
                "to": int(time.time()),
            }

            all_history_data = self.fetch_by_curl_util.fetch_by_curl(
                self.url, params=params
            )
            if all_history_data["s"] == "no_data":
                return None
            return all_history_data
        else:
            raise self.extraction_exception.extraction_method_error(
                "Invalid extract_method"
            )

    def extract_history_data_from_to(
        self,
        from_datetime: str,  # format: "YYYY-MM-DD HH:MM:SS"
        to_datetime: str,  # format: "YYYY-MM-DD HH:MM:SS"
    ):
        if self.extract_method == "curl":
            from_timestamp = self.convert_datetime_util.convert_datetime_to_timestamp(
                from_datetime
            )
            to_timestamp = self.convert_datetime_util.convert_datetime_to_timestamp(
                to_datetime
            )
            if from_timestamp <= to_timestamp:
                params = {
                    "symbol": self.symbol,
                    "resolution": self.resolution,
                    "from": from_timestamp,
                    "to": to_timestamp,
                }

                history_from_to_data = self.fetch_by_curl_util.fetch_by_curl(
                    self.url, params=params
                )
                if history_from_to_data["s"] == "no_data":
                    return None
                return history_from_to_data
            else:
                raise self.validation_exception.validation_error(
                    "from_datetime must be less than or equal to to_datetime"
                )
        else:
            raise self.extraction_exception.extraction_method_error(
                "Invalid extract_method"
            )

    def extract_realtime_data_periodically(
        self,
        look_back_period: str = "10M",
        interval_seconds: str = "60S",  # for example, look_back_period = "10M" means 10 minutes, interval_seconds = "60S" means 60 seconds
    ):
        if self.extract_method == "curl":
            look_back_seconds = self.convert_datetime_util.convert_period_to_seconds(
                look_back_period
            )
            interval = self.convert_datetime_util.convert_period_to_seconds(
                interval_seconds
            )

            while True:
                now = int(time.time())
                params = {
                    "symbol": self.symbol,
                    "resolution": self.resolution,
                    "from": now - look_back_seconds,
                    "to": now,
                }
                real_time_data = self.fetch_by_curl_util.fetch_by_curl(
                    self.url, params=params
                )
                if real_time_data["s"] == "no_data":
                    continue
                else:
                    yield real_time_data
                time.sleep(interval)
        else:
            raise self.extraction_exception.extraction_method_error(
                "Invalid extract_method"
            )
