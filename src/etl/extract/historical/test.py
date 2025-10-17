import requests
import time
import pandas as pd
from datetime import datetime, timedelta, timezone

BASE_URL = "https://fapi.binance.com"
FUNDING_RATE_URL = f"{BASE_URL}/fapi/v1/fundingRate"


def unix_to_datetime(unix_ms):
    return datetime.fromtimestamp(unix_ms / 1000.0, tz=timezone.utc)


def get_funding_rate(symbol, start_time_ms, end_time_ms, limit=1000):
    params = {
        "symbol": symbol,
        "limit": limit,
        "startTime": start_time_ms,
        "endTime": end_time_ms,
    }
    try:
        r = requests.get(FUNDING_RATE_URL, params=params, timeout=30)
        if r.status_code == 200:
            return r.json()
        else:
            print(f"⚠️ Error {r.status_code}: {r.text}")
            return []
    except Exception as e:
        print(f"❌ Exception: {e}")
        return []


def find_earliest_funding_time(
    symbol="BTCUSDT", step_days=90, earliest_year_cutoff=2017
):
    """
    Dò ngược để tìm thời điểm funding rate cũ nhất.
    - Bắt đầu từ now, lùi từng step_days.
    - Ghi lại earliest_found nếu window có dữ liệu.
    - Dừng khi window không có dữ liệu và đã từng thấy dữ liệu ở những window sau đó.
    """
    print(f"\n🔍 Đang dò dữ liệu cũ nhất của {symbol} ...")
    step = timedelta(days=step_days)

    end_dt = datetime.now(timezone.utc)
    start_dt = end_dt - step

    earliest_found = None
    saw_any_data = False

    # Lùi dần cho đến khi gặp một window rỗng sau khi đã thấy dữ liệu -> nghĩa là đã vượt mốc
    while True:
        start_ms = int(start_dt.timestamp() * 1000)
        end_ms = int(end_dt.timestamp() * 1000)

        data = get_funding_rate(symbol, start_ms, end_ms, limit=1000)

        if isinstance(data, list) and len(data) > 0:
            saw_any_data = True
            # dữ liệu trong window, lấy earliest trong batch
            batch_earliest = min(item["fundingTime"] for item in data)
            if earliest_found is None or batch_earliest < earliest_found:
                earliest_found = batch_earliest
            print(
                f"  ▶ Có dữ liệu trong window {start_dt.date()} → {end_dt.date()} (earliest in batch: {unix_to_datetime(batch_earliest)})"
            )
            # tiếp tục lùi thêm để tìm cũ hơn
            end_dt = start_dt
            start_dt = start_dt - step
        else:
            # Nếu window rỗng và trước đó đã thấy dữ liệu thì ta đã vượt mốc -> dừng
            print(
                f"  ▶ Không có dữ liệu trong window {start_dt.date()} → {end_dt.date()}"
            )
            if saw_any_data:
                break
            # Nếu chưa thấy dữ liệu nào, tiếp tục lùi
            end_dt = start_dt
            start_dt = start_dt - step

        # safety cutoff
        if start_dt.year < earliest_year_cutoff:
            print(
                "  ▶ Đã lùi quá ngưỡng năm cắt, dừng dò (khả năng pair chưa tồn tại)."
            )
            break

        # tránh loop quá nhanh (rate limit)
        time.sleep(0.2)

    if earliest_found:
        earliest_dt = unix_to_datetime(earliest_found)
        print(f"\n✅ Earliest fundingTime found: {earliest_dt} (UTC)")
        return earliest_found
    else:
        print("\n❌ Không tìm thấy dữ liệu funding rate cho symbol này.")
        return None


def fetch_all_funding_rates(symbol):
    earliest_ts = find_earliest_funding_time(symbol)
    if earliest_ts is None:
        print("Không thể xác định earliest timestamp. Dừng.")
        return None

    all_data = []
    current_start = earliest_ts
    end_time_ms = int(datetime.now(timezone.utc).timestamp() * 1000)

    print(f"\n🚀 Crawl từ {unix_to_datetime(current_start)} đến hiện tại...")

    while current_start < end_time_ms:
        data = get_funding_rate(symbol, current_start, end_time_ms, limit=1000)
        if not data:
            break
        all_data.extend(data)

        last_time = max(item["fundingTime"] for item in data)
        print(f"  ▸ Lấy {len(data)} bản ghi đến {unix_to_datetime(last_time)}")

        # tiếp tục từ sau last_time
        current_start = last_time + 1
        time.sleep(0.3)

        if len(data) < 1000:
            # đã lấy hết
            break

    if not all_data:
        print("Không có dữ liệu để lưu.")
        return None

    df = pd.DataFrame(all_data)
    df.drop_duplicates(subset=["fundingTime"], inplace=True)
    df["fundingTime"] = df["fundingTime"].apply(unix_to_datetime)
    df = df.sort_values("fundingTime").reset_index(drop=True)

    filename = f"funding_rate_{symbol.lower()}.csv"
    df.to_csv(filename, index=False)
    print(f"\n✅ Lưu {len(df)} dòng vào {filename}")
    print(f"🕒 Khoảng: {df['fundingTime'].iloc[0]} → {df['fundingTime'].iloc[-1]}")
    return df


if __name__ == "__main__":
    symbol = "BTCUSDT"
    fetch_all_funding_rates(symbol)
