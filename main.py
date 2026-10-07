from src.projects.stock.load.raw.load_raw_stock_candlestick import LoadRawStockPrice

test = LoadRawStockPrice(symbol="ACB", resolution="1M")
test.load_raw_data()
