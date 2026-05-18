from datetime import datetime

class TimeUtil:
    @staticmethod
    def convert_unix_second_to_time(unix_second):
        return datetime.fromtimestamp(unix_second)