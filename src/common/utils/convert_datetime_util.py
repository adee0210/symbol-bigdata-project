from datetime import datetime, timezone


class ConvertDatetimeUtil:
    @staticmethod
    def unix_second_to_datetime_utc(unix_second: int):
        return datetime.fromtimestamp(timestamp=unix_second, tz=timezone.utc).replace(
            microsecond=0
        )

    @staticmethod
    def unix_milisecond_to_datetime_utc(unix_milisecond: int):
        return datetime.fromtimestamp(
            timestamp=unix_milisecond / 1000, tz=timezone.utc
        ).replace(microsecond=0)

    @staticmethod
    def from_isodatetime_to_datetime(isodatetime: str):
        if isodatetime.endswith("Z"):
            iso_str = isodatetime.replace("Z", "+00:00")
            return datetime.fromisoformat(iso_str).replace(microsecond=0)
