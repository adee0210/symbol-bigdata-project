from src.extract.extract_stock_candlestick import ExtractStockCandlestick
from src.load.raw.load_raw_stock_candlestick import LoadRawStockPrice

test = LoadRawStockPrice("VNM", "1")
data = ExtractStockCandlestick("VNM", "1", "curl").extract_all_history_data()
print(data)
test.load_raw_data(data)
test.close()
