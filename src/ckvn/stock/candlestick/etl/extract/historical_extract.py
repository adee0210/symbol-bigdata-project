from ckvn.stock.candlestick.configs.config import SYMBOL
from ckvn.stock.candlestick.etl.extract.historical_extract_interface import (
    HistoricalExtractInteface,
)


class HistoricalExtract(HistoricalExtractInteface):
    def __init__(self) -> None:
        self.investing_api = SYMBOL["investing_api"]
        self.symbol = [SYMBOL[s].keys() for s in SYMBOL.keys()]
