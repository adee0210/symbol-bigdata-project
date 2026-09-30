import os
from datetime import datetime, timezone

from curl_cffi import requests
from dotenv import load_dotenv

load_dotenv()


class DiscordUtil:
    def __init__(self, discord_webhook_url=None):

        self.discord_webhook_url = discord_webhook_url or os.getenv(
            "DISCORD_WEBHOOK_URL"
        )

    def send_embed(self, title: str, description: str, color: int):
        if not self.discord_webhook_url:
            print("Discord webhook URL is not configured.")
            return

        data = {
            "embeds": [
                {
                    "title": title,
                    "description": description,
                    "color": color,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
            ]
        }
        try:
            resp = requests.post(self.discord_webhook_url, json=data)
            if resp.status_code not in (200, 204):
                print(f"Failed to send discord message: {resp.status_code}")
        except Exception as e:  # noqa: BLE001
            print(f"Error sending discord message: {e}")

    def notify_info(self, source: str, message: str):
        # Blue color for general info/startup (ANSI: \x1b[1;34m)
        self.send_embed(
            "START",
            f"**Source:** `{source}`\n\n**Message:**\n```ansi\n\x1b[1;34m{message}\x1b[0m\n```",
            3447003,
        )

    def notify_error(self, source: str, message: str):
        # Red color for errors (ANSI: \x1b[1;31m)
        self.send_embed(
            "ERROR",
            f"**Source:** `{source}`\n\n**Message:**\n```ansi\n\x1b[1;31m{message}\x1b[0m\n```",
            16711680,
        )

    def notify_warning(self, source: str, message: str):

        # Yellow color for warnings/stopping (ANSI: \x1b[1;33m)
        self.send_embed(
            "STOP",
            f"**Source:** `{source}`\n\n**Message:**\n```ansi\n\x1b[1;33m{message}\x1b[0m\n```",
            16776960,
        )

    def notify_success(self, source: str, message: str):
        # Green color for success (ANSI: \x1b[1;32m)
        self.send_embed(
            "SUCCESS",
            f"**Source:** `{source}`\n\n**Message:**\n```ansi\n\x1b[1;32m{message}\x1b[0m\n```",
            65280,
        )


if __name__ == "__main__":
    discord = DiscordUtil()
    discord.notify_info("main.py", "Program has started successfully...")
    discord.notify_error(
        "src/extract/extract_stock_candlestick.py",
        "Exception: Failed to connect to Database",
    )
    discord.notify_warning("main.py", "Program is stopping...")
    discord.notify_success(
        "src/extract/extract_stock_candlestick.py",
        "Candlestick data extraction completed!",
    )
