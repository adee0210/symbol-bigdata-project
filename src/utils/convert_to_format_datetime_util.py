from datetime import datetime


class ConvertToFormatDatetimeUtil:
    @staticmethod
    def unix_second_to_datetime(unix_second_time):
        r = datetime.fromtimestamp(unix_second_time).strftime("%Y-%m-%d %H:%M:%S")
        return r

    def unix_milisecond_to_datetime(unix_milisecond_time):
        r = datetime.fromtimestamp(unix_milisecond_time / 1000).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return r

    def isoformat_time_to_datetime(isoformat_time):
        isoformat_time = isoformat_time.replace("Z", "+00:00")
        dt = datetime.fromisoformat(isoformat_time)
        r = dt.strftime("%Y-%m-%d %H:%M:%S")
        return r
