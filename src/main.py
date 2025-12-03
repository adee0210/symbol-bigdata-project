import sys
from pathlib import Path

from utils.selenium_util import SeleniumUtil
from vn.candlestick_data_pipeline.extract.historical_extract.etf_1minute_historical_extract import (
    ETF1MinuteHistoricalExtract,
)


def find_project_root(current_file, marker="requirements.txt"):
    current_path = Path(current_file).resolve()
    for parent in current_path.parents:
        if (parent / marker).exists():
            return parent
    return current_path.parent


project_root = find_project_root(__file__, marker="requirements.txt")
sys.path.insert(0, str(project_root))

test = SeleniumUtil(
    url="https://tvc4.investing.com/4379fbb3b2cf9327a768dbfde5d69d1d/1761556750/52/52/110/history?symbol=E1VFVN30&resolution=1&from=1609459200&to=1672531199"
)
data = test.get_data_by_tag_name(tag_name="body")
data = data["t"]
print(len(data))
