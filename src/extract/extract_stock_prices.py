import json

from curl_cffi import requests

url = "https://histdatafeed.vps.com.vn/tradingview/history?symbol=ACB&resolution=1D&from=1748217600&to=1788998400&countback=330"

# Giả lập hoàn toàn trình duyệt Chrome
response = requests.get(url)

if response.status_code == 200:
    print(" Lấy dữ liệu thành công!")
    data = response.json()
    with open("data/data.json", "w") as f:
        json.dump(data, f)
    print(data)
else:
    print(f"Lỗi: {response.status_code}")