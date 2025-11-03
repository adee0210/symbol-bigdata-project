import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import requests
from configs.logger_config import LoggerConfig
from configs.variable_config import CMC_CONFIG


class CMCHistoricalExtract:
    def __init__(self) -> None:
        self.logger = LoggerConfig.logger_config("CMCHistoricalExtract")


# Tham số có thể thay đổi
day = 1
start_time = 1600000000  # 2020
end_time = start_time + 86400 * day  # Tính end_time dựa trên day
symbol_id = 1027

# Cập nhật URL để bao gồm timeEnd nếu API hỗ trợ
url = (
    CMC_CONFIG["cmc_historical_url"]
    .replace("symbol_id", str(symbol_id))
    .replace("symbol_time_start", str(start_time))
    .replace("symbol_time_end", str(end_time))
)

print(f"URL: {url}")

r = requests.get(url)
print(f"Status code: {r.status_code}")
if r.status_code == 200:
    with open("data.json", "w") as f:
        json.dump(r.json(), f)

    data = r.json()["data"]["quotes"]
    print(f"First quote: {data[0]}")
    print(f"Last quote: {data[-1]}")
    print(f"Length of data: {len(data)}")
