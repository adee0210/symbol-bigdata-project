from src.projects.stock.repository.repository_stock_candlestick import (
    RepositoryStockCandlestick,
)


class LoadRawStockPrice:
    def __init__(self, symbol: str, resolution: str):
        self.symbol = symbol
        self.resolution = resolution
        self.repository_candlestick = RepositoryStockCandlestick(connection="Oracle")

    def load_raw_data(self, data: dict):
        self.repository_candlestick.insert_stock_candlestick_data(data)
