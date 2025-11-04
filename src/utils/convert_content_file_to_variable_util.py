import json
from pathlib import Path
import os


class ConvertContentFileToVariableUtil:

    @staticmethod
    def symbol_top100_to_list():
        base_dir = Path(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    )
                )
            )
        )

        for file in base_dir.rglob("top100_symbol_with_id.json"):
            content = file.read_text(encoding="utf-8")
            top100_symbol = json.loads(content)
        return top100_symbol

    @staticmethod
    def get_top100_symbol():
        top100_symbol = [
            data["symbol"]
            for data in ConvertContentFileToVariableUtil.symbol_top100_to_list()
        ]
        return top100_symbol

    @staticmethod
    def get_top100_symbol_id():
        top100_symbol_id = [
            data["id"]
            for data in ConvertContentFileToVariableUtil.symbol_top100_to_list()
        ]
        return top100_symbol_id
