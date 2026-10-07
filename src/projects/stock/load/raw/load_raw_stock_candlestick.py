from common.utils.util_load_raw_json_file import LoadRawJsonFile
from src.projects.stock.extract.extract_stock_candlestick import ExtractStockCandlestick


class LoadRawStockPrice:
    def __init__(self, symbol: str, resolution: str):
        self.symbol = symbol
        self.resolution = resolution
        self.extract_candlestick = ExtractStockCandlestick(
            self.symbol, self.resolution, "curl"
        )
        # self.repository_candlestick = RepositoryStockCandlestick(connection="Oracle")
        self.raw_json_loader = LoadRawJsonFile(
            file_name="test",
            file_path=f"data/raw/stock/candlestick/{self.symbol}_{self.resolution}.json",
        )

    def load_raw_data(self):
        data = self.extract_candlestick.extract_all_history_data()
        self.raw_json_loader.load_api_to_json_file(data)

        # self.repository_candlestick.insert_stock_candlestick_data(data)
