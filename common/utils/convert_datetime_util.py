from datetime import datetime, timezone

from common.exception.validation_exception import ValidationException


class ConvertDatetimeUtil:
    def __init__(self) -> None:
        self.validation_exception = ValidationException("Validation error")

    def convert_datetime_to_timestamp(self, datetime_str):
        # Convert a datetime string in the format "YYYY-MM-DD HH:MM:SS" to a Unix timestamp

        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=timezone.utc
        )
        timestamp = int(dt.timestamp())

        return timestamp

    def convert_timestamp_to_datetime(self, timestamp):
        # Convert a Unix timestamp to a datetime in the format "YYYY-MM-DD HH:MM:SS"

        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)

        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def convert_resolution(self, resolution: str):
        # convert resolution to the format used by the API, e.g., "1M" to "1", "5M" to "5", etc.
        if resolution not in ["1M", "5M", "15M", "30M", "1H", "1D", "1W", "1MO"]:
            raise self.validation_exception.validation_error("Invalid resolution")
        resolution_mapping = {
            "1M": "1",
            "5M": "5",
            "15M": "15",
            "30M": "30",
            "1H": "60",
            "1D": "1D",
            "1W": "1W",
            "1MO": "1M",
        }

        return resolution_mapping[resolution]

    def convert_period_to_seconds(self, period: str):
        # Convert a positive duration such as 10M or 2H to seconds.
        if not isinstance(period, str) or len(period) < 2:
            raise self.validation_exception.validation_error("Period must be a positive integer followed by a unit.")

        try:
            value = int(period[:-1])
        except ValueError as exc:
            raise self.validation_exception.validation_error(
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
            raise self.validation_exception.validation_error(
                "Period must be a positive integer followed by S, M, H, D, or W."
            )

        return value * units[unit]
