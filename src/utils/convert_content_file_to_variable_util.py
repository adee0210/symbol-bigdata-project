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

        for file in base_dir.rglob("top100_symbol.txt"):
            content = file.read_text(encoding="utf-8")
            top100_symbol_name = json.loads(content)
        return top100_symbol_name
