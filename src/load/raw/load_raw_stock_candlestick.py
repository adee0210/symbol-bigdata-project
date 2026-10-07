from common.database.oracle import OracleConfig
from src.extract.extract_stock_candlestick import ExtractStockCandlestick


class LoadRawStockPrice:
    def __init__(self, symbol: str, resolution: str):
        self.oracle_config = OracleConfig()
        self.connection = self.oracle_config.get_connection()

        self.symbol = symbol
        self.resolution = resolution

    def load_raw_data(self, data: dict):
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

        rows = []

        total = len(data["t"])

        for i in range(total):
            rows.append(
                {
                    "symbol": self.symbol,
                    "resolution": self.resolution,
                    "timestamp": int(data["t"][i]),
                    "open": float(data["o"][i]),
                    "high": float(data["h"][i]),
                    "low": float(data["l"][i]),
                    "close": float(data["c"][i]),
                    "volume": int(data["v"][i]),
                }
            )

        cursor = self.connection.cursor()

        try:
            cursor.executemany(sql, rows)
            self.connection.commit()

            print(f"Successfully insert {len(rows)} records.")

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()
            self.oracle_config.release_connection(self.connection)

    def load_raw_data_from_to(self, data: dict):
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

        rows = []

        total = len(data["t"])

        for i in range(total):
            rows.append(
                {
                    "symbol": self.symbol,
                    "resolution": self.resolution,
                    "timestamp": int(data["t"][i]),
                    "open": float(data["o"][i]),
                    "high": float(data["h"][i]),
                    "low": float(data["l"][i]),
                    "close": float(data["c"][i]),
                    "volume": int(data["v"][i]),
                }
            )

        cursor = self.connection.cursor()

        try:
            cursor.executemany(sql, rows)
            self.connection.commit()

            print(f"Successfully insert {len(rows)} records.")

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()
            self.oracle_config.release_connection(self.connection)
