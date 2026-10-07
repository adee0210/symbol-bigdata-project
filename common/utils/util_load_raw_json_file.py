import json
from pathlib import Path

from common.exception.exception_storage import ExceptionStorage


class LoadRawJsonFile:
    def __init__(self, file_name: str, file_path: str):
        self.file_name = file_name
        self.file_path = Path(file_path)
        self.exception_storage = ExceptionStorage("Storage error")

    def load_api_to_json_file(self, data):
        """Load data from API to a JSON file."""
        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.file_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        except OSError as e:
            raise self.exception_storage.storage_write_error(
                f"Failed to write data to {self.file_path}: {e}"
            )
