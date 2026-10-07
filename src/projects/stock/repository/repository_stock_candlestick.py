from common.database.database_oracle import DatabaseOracle
from common.exception.exception_validation import ExceptionValidation
from common.logging.logging_logger import LoggingLogger
from src.projects.stock.models.model_stock_candlestick import ModelStockCandlestick


class RepositoryStockCandlestick:
    def __init__(self, connection="Oracle"):
        self.validation_exception = ExceptionValidation("Validation Error")
        self.logging_logger = LoggingLogger()
        if connection == "Oracle":
            self.oracle = DatabaseOracle()
            self.connection = self.oracle.get_connection()
        else:
            raise self.validation_exception.validation_error(
                "Invalid connection type. Only 'Oracle' is supported."
            )

    def insert_stock_candlestick_data(self, data: dict):
        sql = """
            INSERT INTO RAW_STOCK_CANDLESTICK (
                SYMBOL,
                RESOLUTION,
                TIMESTAMP,
                OPEN,
                HIGH,
                LOW,
                CLOSE,
                VOLUME
            )
            VALUES (
                :symbol,
                :resolution,
                :timestamp,
                :open,
                :high,
                :low,
                :close,
                :volume
            )
        """

        required_series = ("t", "o", "h", "l", "c", "v")
        try:
            total = len(data["t"])
            if any(len(data[key]) != total for key in required_series[1:]):
                raise self.validation_exception.validation_error(
                    "Candlestick series must have the same length."
                )
        except KeyError as exc:
            raise self.validation_exception.validation_error(
                f"Missing candlestick field: {exc.args[0]}"
            ) from exc

        rows = []

        for i in range(total):
            candlestick = ModelStockCandlestick(
                symbol=data["symbol"],
                resolution=data["resolution"],
                timestamp=data["t"][i],
                open=data["o"][i],
                high=data["h"][i],
                low=data["l"][i],
                close=data["c"][i],
                volume=data["v"][i],
            )
            rows.append(candlestick.dict())

        cursor = self.connection.cursor()

        try:
            cursor.executemany(sql, rows)
            self.connection.commit()

            print(f"Successfully inserted {len(rows)} records.")
        except Exception:
            self.connection.rollback()
            cursor.close()
            raise
        finally:
            cursor.close()
