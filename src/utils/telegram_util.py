import requests
import time
from configs.variable_config import TELEGRAM_CONFIG
from configs.logger_config import LoggerConfig


class TelegramUtils:

    def __init__(self):
        try:
            self.logger = LoggerConfig.logger_config("TelegramUtils")
            self.bot_token = TELEGRAM_CONFIG.get("bot_token")
            self.chat_id = TELEGRAM_CONFIG.get("chat_id")
            self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
            self.logger.info("Telegram utils initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize Telegram utils: {str(e)}")
            raise

    def send_alert(self, title: str, message: str, level: str = "INFO") -> bool:
        if not self.bot_token or not self.chat_id:
            self.logger.warning("Telegram bot token or chat ID not configured")
            return False

        try:
            emoji_map = {
                "INFO": "ℹ️",
                "WARNING": "⚠️",
                "ERROR": "❌",
                "SUCCESS": "✅",
            }

            emoji = emoji_map.get(level.upper(), "📢")

            formatted_message = f"{emoji} *{title}*\n\n{message}"

            if level.upper() in ["WARNING", "ERROR"]:
                formatted_message += (
                    f"\n\n🕒 Time: {time.strftime('%Y-%m-%d %H:%M:%S')}"
                )

            data = {
                "chat_id": self.chat_id,
                "text": formatted_message,
                "parse_mode": "Markdown",
            }

            url = f"{self.base_url}/sendMessage"
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()

            self.logger.info(f"Telegram alert sent successfully: {title}")
            return True

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error sending Telegram alert: {str(e)}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error sending Telegram alert: {str(e)}")
            return False

    def send_message(self, message: str) -> bool:
        """Send a simple message to Telegram"""
        try:
            if not self.bot_token or not self.chat_id:
                self.logger.warning("Telegram bot token or chat ID not configured")
                return False

            data = {"chat_id": self.chat_id, "text": message, "parse_mode": "Markdown"}

            url = f"{self.base_url}/sendMessage"
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()

            self.logger.info("Telegram message sent successfully")
            return True

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error sending Telegram message: {str(e)}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error sending Telegram message: {str(e)}")
            return False
