import requests
import time
import pandas as pd
from datetime import datetime, timedelta

# API endpoint
BASE_URL = "https://fapi.binance.com"
FUNDING_RATE_URL = f"{BASE_URL}/fapi/v1/fundingRate"


# Lấy lịch sử funding rate cho BTCUSDT
def get_historical_funding_rate(symbol, start_time, end_time, limit=1000):
    params = {
        "symbol": symbol,
        "limit": limit,
        "startTime": start_time,
        "endTime": end_time,
    }
    try:
        response = requests.get(FUNDING_RATE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching {symbol}: {response.status_code}")
            return []
    except Exception as e:
        print(f"Exception for {symbol}: {e}")
        return []


def unix_to_datetime(unix_ms):
    return datetime.fromtimestamp(unix_ms / 1000.0)


def fetch_btc_funding_rates():
    symbol = "BTCUSDT"
    all_data = []

    start_time = int(datetime(2019, 8, 1).timestamp() * 1000)
    end_time = int(datetime.now().timestamp() * 1000)  # Hiện tại

    print(f"Fetching funding rate history for {symbol}...")
    current_start = start_time

    while current_start < end_time:
        data = get_historical_funding_rate(symbol, current_start, end_time)
        if not data:
            break
        all_data.extend(data)

        if len(data) < 1000:
            break  # Đã lấy hết dữ liệu
        last_time = max([item["fundingTime"] for item in data])
        current_start = last_time + 1  # Tiếp tục từ thời điểm cuối

        print(f"Fetched {len(data)} records up to {unix_to_datetime(last_time)}")
        time.sleep(0.5)  # Tránh rate limit

    # Lưu vào CSV
    if all_data:
        df = pd.DataFrame(all_data)
        df["fundingTime"] = df["fundingTime"].apply(unix_to_datetime)
        df.to_csv("binance_btc_funding_rates.csv", index=False)
        print("Data saved to binance_btc_funding_rates.csv")

    return all_data


# Chạy script
if __name__ == "__main__":
    funding_rates = fetch_btc_funding_rates()
    print(f"Total records fetched: {len(funding_rates)}")
