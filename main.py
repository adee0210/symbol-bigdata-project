from src.extract.extract_stock_prices import ExtractStockPrices

test = ExtractStockPrices("VCB", "1")

data = test.extract_realtime_data_periodically(
    look_back_period="10M", interval_seconds="60S"
)

for item in data:
    print(item)
