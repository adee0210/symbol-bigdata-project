import sys
from pathlib import Path

from utils.convert_to_format_datetime_util import ConvertToFormatDatetimeUtil
from utils.selenium_util import SeleniumUtil
from vn.candlestick_data_pipeline.extract.historical_extract.etf_1minute_historical_extract import (
    ETF1MinuteHistoricalExtract,
)

sys.path.insert(0, str(project_root))

from configs.config import PG_URL_CONFIG, VN_CANDLESTICK_DATA_CONFIG


def find_project_root(current_file, marker="requirements.txt"):
    current_path = Path(current_file).resolve()
    for parent in current_path.parents:
        if (parent / marker).exists():
            return parent
    return current_path.parent


project_root = find_project_root(__file__, marker="requirements.txt")
sys.path.insert(0, str(project_root))


test = ETF1MinuteHistoricalExtract()
test.extract_logic()
