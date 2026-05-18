import requests

data = requests.get(url="https://histdatafeed.vps.com.vn/tradingview/history?symbol=ACB&resolution=1&from=1738454400&to=1779148800&countback=329")
print(data.json())