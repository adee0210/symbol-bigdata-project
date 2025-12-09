import os

from dotenv import load_dotenv


load_dotenv()

VN_CANDLESTICK_DATA_CONFIG = {
    "vn_candlestick_datasource_url": os.getenv("VN_CANDLESTICK_DATASOURCE_URL")
}


TELEGRAM_CONFIG = {
    "telegram_bot_token": os.getenv("TELEGRAM_BOT_TOKEN"),
    "telegram_chat_id": os.getenv("TELEGRAM_CHAT_ID"),
}

HDFS_CONFIG = {
    "hdfs_host": os.getenv("HDFS_HOST"),
    "hdfs_port": os.getenv("HDFS_PORT"),
    "hdfs_user": os.getenv("HDFS_USER"),
}
