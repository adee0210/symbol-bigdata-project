import requests
import json


# Lấy funding rate hiện tại cho tất cả coin
def get_current_funding_rates():
    url = "https://fapi.binance.com/fapi/v1/premiumIndex"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Lọc chỉ perpetual futures (nếu cần)
        perpetuals = [
            item for item in data if "USDT" in item["symbol"] or "USD" in item["symbol"]
        ]  # Ví dụ lọc USDT/USD pairs
        return perpetuals
    else:
        print(f"Error: {response.status_code}")
        return None


# Lấy lịch sử funding rate cho một symbol
def get_historical_funding_rate(symbol, limit=1000):
    url = f"https://fapi.binance.com/fapi/v1/fundingRate?symbol={symbol}&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


# Ví dụ sử dụng
current_rates = get_current_funding_rates()
if current_rates:
    print(json.dumps(current_rates[:5], indent=4))  # In 5 cái đầu tiên

historical = get_historical_funding_rate("BTCUSDT")
if historical:
    print(json.dumps(historical[:5], indent=4))  # In 5 records đầu
