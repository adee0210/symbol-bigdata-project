import time
from src.utils.fetch_by_curl_util import FetchByCurlUtil
from src.utils.convert_datetime_util import ConvertDatimeUtil
from src.utils.check_format_datetime_util import CheckFormatDatetimeUtil


class ExtractStockPrices:
    def __init__(self, symbol, resolution: str):
        self.url = "https://histdatafeed.vps.com.vn/tradingview/history"
        self.symbol = symbol
        if resolution.strip().upper() not in ["1", "5", "1H", "1D", "1W", "1M"]:
            raise ValueError(
                "Invalid resolution. Must be one of '1', '5', '1H', '1D', '1W', or '1M'."
            )
        self.resolution = resolution

    def extract_all_history_data(self):
        params = {
            "symbol": self.symbol,
            "resolution": self.resolution,
            "from": int(time.time()) - 50 * 365 * 24 * 60 * 60,  # 50 years ago
            "to": int(time.time()),
        }

        all_history_data = FetchByCurlUtil.fetch_by_curl(self.url, params=params)
        return all_history_data

    def extract_history_data_from_to(
        self, from_datetime: str, to_datetime: str, timezone="Asia/Ho_Chi_Minh"
    ):

        from_timestamp = ConvertDatimeUtil.convert_datetime_to_timestamp(from_datetime)
        to_timestamp = ConvertDatimeUtil.convert_datetime_to_timestamp(to_datetime)
        if from_timestamp <= to_timestamp:
            params = {
                "symbol": self.symbol,
                "resolution": self.resolution,
                "from": from_timestamp,
                "to": to_timestamp,
            }

            history_from_to_data = FetchByCurlUtil.fetch_by_curl(
                self.url, params=params
            )
            return history_from_to_data
        else:
            raise ValueError("from_datetime must be less than or equal to to_datetime")

    def extract_realtime_data_periodically(
        self, look_back_period: str = "10M", interval_seconds: str = "60S"
    ):
        look_back_seconds = ConvertDatimeUtil.convert_period_to_seconds(
            look_back_period
        )
        interval = ConvertDatimeUtil.convert_period_to_seconds(interval_seconds)

        while True:
            now = int(time.time())
            params = {
                "symbol": self.symbol,
                "resolution": self.resolution,
                "from": now - look_back_seconds,
                "to": now,
            }
            yield FetchByCurlUtil.fetch_by_curl(self.url, params=params)
            time.sleep(interval)
