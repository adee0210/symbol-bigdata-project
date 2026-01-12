from abc import ABC, abstractmethod


class HistoricalInterface(ABC):
    @abstractmethod
    def historical_extract(self):
        pass
