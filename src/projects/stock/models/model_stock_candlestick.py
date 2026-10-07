from pydantic.v1 import BaseModel


class ModelStockCandlestick(BaseModel):
    symbol: str
    resolution: str
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: int
