from datetime import timedelta, datetime, timezone
import json
from pathlib import Path
import os
import time
import pandas as pd

import requests
from configs.logger_config import LoggerConfig
from configs.variable_config import BINANCE_FUNDING_RATE_CONFIG
from utils.convert_datetime_util import ConvertDatetimeUtil


class BinanceFundingRateHistoricalExtract:
    def __init__(self) -> None:
        try:
            self.logger = LoggerConfig.logger_config(
                "Binance Fundingrate historical extract"
            )

            self.binance_funding_rate_url = BINANCE_FUNDING_RATE_CONFIG[
                "binance_funding_rate_url"
            ]

            base_dir = Path(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                        )
                    )
                )
            )

            for file in base_dir.rglob("top100_symbol.txt"):
                content = file.read_text(encoding="utf-8")
                top100_symbol_name = json.loads(content)
                self.top100_symbol_name_upper_with_usdt = [
                    f"{symbol_name.upper()}usdt" for symbol_name in top100_symbol_name
                ]

        except Exception as e:
            self.logger.error(
                f"Cannot load Binance funding rate historical data configurations: Error {str(e)}"
            )

    def get_funding_rate_from_api_as_json(
        self, symbol, start_unixtime_ms, end_unixtime_ms, limit=1000
    ):

        params = {
            "symbol": symbol,
            "limit": limit,
            "startTime": start_unixtime_ms,
            "endTime": end_unixtime_ms,
        }

        try:
            r = requests.get(self.binance_funding_rate_url, params=params, timeout=30)
            if r.status_code == 200:
                self.logger.info(
                    "Successfully retrieved funding rate data from API request"
                )
                return r.json()
            else:
                self.logger.error(
                    f"Failed to get funding rate: {r.status_code}: {r.text}"
                )
                return []
        except Exception as e:
            self.logger.error(f"API request failed with exception: {e}")
            return []

    def find_earliest_funding_time(
        self, symbol, step_days=90, earliest_year_cutoff=2015
    ):
        step = timedelta(days=step_days)

        end_datetime = datetime.now(timezone.utc)
        start_datetime = end_datetime - step
        check_any_data = False
        earliest_found = None

        self.logger.info(f"Searching for earliest funding rate data for {symbol}")

        while True:
            start_unixtime_ms = int(start_datetime.timestamp() * 1000)
            end_unixtime_ms = int(end_datetime.timestamp() * 1000)

            data = self.get_funding_rate_from_api_as_json(
                symbol=symbol,
                start_unixtime_ms=start_unixtime_ms,
                end_unixtime_ms=end_unixtime_ms,
            )

            if isinstance(data, list) and len(data) > 0:
                check_any_data = True
                batch_earliest = min(item["fundingTime"] for item in data)
                if earliest_found is None or batch_earliest < earliest_found:
                    earliest_found = batch_earliest
                self.logger.info(
                    f"Found data in period: {start_datetime.date()} to {end_datetime.date()}"
                )

                end_datetime = start_datetime
                start_datetime = start_datetime - step
            else:
                self.logger.warning(
                    f"No data found in period: {start_datetime.date()} to {end_datetime.date()}"
                )
                if check_any_data:
                    break
                end_datetime = start_datetime
                start_datetime = start_datetime - step

            if start_datetime.year < earliest_year_cutoff:
                self.logger.warning(
                    f"Reached year cutoff threshold: {earliest_year_cutoff}"
                )
                break
            time.sleep(0.2)

        if earliest_found:
            earliest_datetime = ConvertDatetimeUtil.unix_to_datetime(earliest_found)
            self.logger.info(f"Earliest funding time found: {earliest_datetime}")
            return earliest_found
        else:
            self.logger.warning("No data found for this symbol")
            return None

    def extract(self, symbol=None):
        if symbol is None:
            symbol = self.top100_symbol_name_upper_with_usdt[0]

        self.logger.info(f"Starting extraction for symbol: {symbol}")
        earliest_ts = self.find_earliest_funding_time(symbol)

        if earliest_ts is None:
            self.logger.error(
                "Cannot determine earliest timestamp. Stopping extraction."
            )
            return None

        all_data = []
        current_start = earliest_ts
        end_time_ms = int(datetime.now(timezone.utc).timestamp() * 1000)

        self.logger.info(
            f"Extracting data from {ConvertDatetimeUtil.unix_to_datetime(current_start)} to present"
        )

        while current_start < end_time_ms:
            data = self.get_funding_rate_from_api_as_json(
                symbol=symbol,
                start_unixtime_ms=current_start,
                end_unixtime_ms=end_time_ms,
                limit=1000,
            )
            if not data:
                break
            all_data.extend(data)

            last_time = max(item["fundingTime"] for item in data)
            self.logger.info(
                f"Retrieved {len(data)} records up to {ConvertDatetimeUtil.unix_to_datetime(last_time)}"
            )

            current_start = last_time + 1
            time.sleep(0.3)

            if len(data) < 1000:
                break

        if not all_data:
            self.logger.warning("No data to save")
            return None

        df = pd.DataFrame(all_data)
        df.drop_duplicates(subset=["fundingTime"], inplace=True)
        df["fundingTime"] = df["fundingTime"].apply(
            ConvertDatetimeUtil.unix_to_datetime
        )
        df = df.sort_values("fundingTime").reset_index(drop=True)

        filename = f"funding_rate_{symbol.lower()}.csv"
        df.to_csv(filename, index=False)
        self.logger.info(f"Saved {len(df)} rows to {filename}")
        self.logger.info(
            f"Data range: {df['fundingTime'].iloc[0]} to {df['fundingTime'].iloc[-1]}"
        )
        return df
