from abc import ABC, abstractmethod


class HistoricalExtractInterface(ABC):
    @abstractmethod
    def historical_extract_logic(self):
        pass

    @abstractmethod
    def historical_extract(self):
        pass
