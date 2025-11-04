import datetime
import os
from dotenv import load_dotenv
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
from src.utils.convert_content_file_to_variable_util import (
    ConvertContentFileToVariableUtil,
)


load_dotenv()

POSTGRES_CONFIG = {
    "host": os.getenv("PG_HOST"),
    "port": os.getenv("PG_PORT"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
    "database": os.getenv("PG_DATABASE"),
    "min_size": 5,
    "max_size": 20,
}

CMC_CONFIG = {
    "cmc_realtime_key": os.getenv("CMC_KEY"),
    "cmc_realtime_interval_send_request": 260,
    "cmc_realtime_url": f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD",
    "cmc_realtime_table_in_pg": "cmc",
    "cmc_historical_url": "https://api.coinmarketcap.com/data-api/v3.1/cryptocurrency/historical?id=symbol_id&convertId=2781&timeStart=symbol_time_start&timeEnd=symbol_time_end&interval=15m",
    "cmc_historical_batch_extract": 5000,
    "cmc_historical_time_end": datetime.datetime.now().timestamp(),
    "cmc_historical_day": 4,
}


BINANCE_FUNDING_RATE_CONFIG = {
    "binance_funding_rate_url": "https://fapi.binance.com/fapi/v1/fundingRate",
    "binance_funding_rate_table_in_pg": "binance_funding_rate",
}

TOP100_SYMBOL_CONFIG = ConvertContentFileToVariableUtil.symbol_top100_to_list()

TELEGRAM_CONFIG = {
    "bot_token": os.getenv("TELEGRAM_BOT_TOKEN"),
    "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
}
