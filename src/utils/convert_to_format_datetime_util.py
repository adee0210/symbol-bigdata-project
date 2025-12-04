from datetime import datetime


class ConvertToFormatDatetimeUtil:
    @staticmethod
    def unix_second_to_datetime(unix_second_time):
        r = datetime.fromtimestamp(unix_second_time).replace(microsecond=0)
        return r

    @staticmethod
    def unix_milisecond_to_datetime(unix_milisecond_time):
        r = datetime.fromtimestamp(unix_milisecond_time / 1000).replace(microsecond=0)
        return r

    @staticmethod
    def isoformat_time_to_datetime(isoformat_time):
        r = datetime.fromisoformat(isoformat_time).replace(microsecond=0)

        return r

    @staticmethod
    def datetime_to_unix_second(datetime):
        r = int(datetime.timestamps())
        return r

    @staticmethod
    def datetime_to_unix_milisecond(datetime):
        r = int(datetime.timestamps() * 1000)
        return r
