from abc import ABC, abstractmethod


class HistoricalExtractInterface(ABC):
    @abstractmethod
    def historical_extract(self):
        pass

    @abstractmethod
    def storage_historical_extract_data(self):
        pass
