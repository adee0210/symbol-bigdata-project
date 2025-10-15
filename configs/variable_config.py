import os
from dotenv import load_dotenv

load_dotenv()

CMC_CONFIG = {
    "cmc_key": os.getenv("CMC_KEY"),
    "cmc_interval_send_request": 260,
    "cmc_url": f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD",
}
