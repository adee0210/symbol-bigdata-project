from datetime import datetime


class ConvertDatetimeUtil:
    @staticmethod
    def unix_second_to_datetime(unix_time):
        return datetime.fromtimestamp(unix_time).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def unix_ms_to_datetime(unix_ms):
        return datetime.fromtimestamp(unix_ms / 1000.0).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def isoformat_datetime_to_datetime(iso_datetime: str):
        dt = datetime.fromisoformat(iso_datetime.replace("Z", "+00:00"))
        local_time = dt.astimezone()
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
