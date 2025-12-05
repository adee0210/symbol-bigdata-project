import json
import sys
from pathlib import Path


def find_project_root(current_file, marker="requirements.txt"):
    current_path = Path(current_file).resolve()
    for parent in current_path.parents:
        if (parent / marker).exists():
            return parent
    return current_path.parent


project_root = find_project_root(__file__, marker="requirements.txt")
sys.path.insert(0, str(project_root))

from utils.selenium_util import SeleniumUtil
from vn.candlestick_data_pipeline.extract.historical_extract.etf_1minute_historical_extract import (
    ETF1MinuteHistoricalExtract,
)

# sele = SeleniumUtil()
# data = sele.get_data_by_tag_name(
#     url="https://tvc4.investing.com/4379fbb3b2cf9327a768dbfde5d69d1d/1761556750/52/52/110/history?symbol=E1VFVN30&resolution=1&from=1609459200&to=1672531199",
#     tag_name="body",
# )
# with open("test.json", "w") as f:
#     json.dump(data, f)

etf = ETF1MinuteHistoricalExtract()
etf.extract_logic()
