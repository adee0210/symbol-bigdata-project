from datetime import datetime


class ConvertDatimeUtil:
    @staticmethod
    def convert_datetime_to_timestamp(datetime_str):
        # Convert a datetime string in the format "YYYY-MM-DD HH:MM:SS" to a Unix timestamp

        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        timestamp = int(dt.timestamp())
        return timestamp

    @staticmethod
    def convert_timestamp_to_datetime(timestamp):
        # Convert a Unix timestamp to a datetime in the format "YYYY-MM-DD HH:MM:SS"

        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def period_to_seconds(period: str):
        # Convert a positive duration such as 10M or 2H to seconds.
        if not isinstance(period, str) or len(period) < 2:
            raise ValueError("Period must be a positive integer followed by a unit.")

        try:
            value = int(period[:-1])
        except ValueError as exc:
            raise ValueError(
                "Period must be a positive integer followed by a unit."
            ) from exc

        units = {
            "S": 1,
            "M": 60,
            "H": 60 * 60,
            "D": 24 * 60 * 60,
            "W": 7 * 24 * 60 * 60,
        }
        unit = period[-1].upper()
        if value <= 0 or unit not in units:
            raise ValueError(
                "Period must be a positive integer followed by S, M, H, D, or W."
            )
        return value * units[unit]
