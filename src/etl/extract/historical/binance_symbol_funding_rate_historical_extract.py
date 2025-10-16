from pathlib import Path
from configs.logger_config import LoggerConfig
from configs.variable_config import CMC_CONFIG


class BinanceFundingRateHistoricalExtract:
    def __init__(self) -> None:
        try:
            self.logger = LoggerConfig.logger_config(
                "Binance Fundingrate historical extract"
            )
            for path in Path(.).rglob("top100_symbol.json"):
                with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)


        except Exception as e:
            self.logger.error(
                f"Can not load Binance fundingrate historical data configurations: Error {str(e)}"
            )
