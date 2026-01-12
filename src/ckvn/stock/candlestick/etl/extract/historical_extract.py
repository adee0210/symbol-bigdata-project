from ckvn.stock.candlestick.configs.config import SYMBOL
from ckvn.stock.candlestick.etl.extract.historical_interface import HistoricalInterface


class HistoricalExtract(HistoricalInterface):
    def __init__(self) -> None:
        self.investing_api = SYMBOL["investing_api"]
        self.symbol = [SYMBOL[s].keys() for s in SYMBOL.keys()]
        
        
