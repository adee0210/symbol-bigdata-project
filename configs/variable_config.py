import os
from dotenv import load_dotenv

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
    "cmc_key": os.getenv("CMC_KEY"),
    "cmc_interval_send_request": 260,
    "cmc_url": f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD",
    "cmc_top100_symbol_name": "top100_symbol.txt",
    "cmc_table_in_pg": "cmc",
}


BINANCE_FUNDING_RATE_CONFIG = {
    "binance_funding_rate_url": "https://fapi.binance.com/fapi/v1/fundingRate",
    "binance_funding_rate_table_in_pg": "binance_funding_rate",
}

TELEGRAM_CONFIG = {
    "bot_token": os.getenv("TELEGRAM_BOT_TOKEN"),
    "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
}
