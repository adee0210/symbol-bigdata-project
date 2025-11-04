from datetime import timedelta, datetime
import time
import pandas as pd

import requests
from configs.logger_config import LoggerConfig
from configs.variable_config import BINANCE_FUNDING_RATE_CONFIG
from utils.convert_content_file_to_variable_util import ConvertContentFileToVariableUtil
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

            self.top100_symbol_name_upper_with_usdt = [
                f"{symbol_name.upper()}usdt"
                for symbol_name in ConvertContentFileToVariableUtil.symbol_top100_to_list()
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

        end_datetime = datetime.now()
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
            earliest_datetime = ConvertDatetimeUtil.unix_ms_to_datetime(earliest_found)
            self.logger.info(f"Earliest funding time found: {earliest_datetime}")
            return earliest_found
        else:
            self.logger.warning("No data found for this symbol")
            return None

    def extract(self):
        symbols = self.top100_symbol_name_upper_with_usdt

        self.logger.info(f"Starting extraction for {len(symbols)} symbols")

        all_dataframes = []
        successful_extractions = 0
        failed_extractions = 0

        for i, symbol in enumerate(symbols, 1):
            self.logger.info(f"Processing symbol {i}/{len(symbols)}: {symbol}")

            try:
                earliest_ts = self.find_earliest_funding_time(symbol)

                if earliest_ts is None:
                    self.logger.error(
                        f"Cannot determine earliest timestamp for {symbol}. Skipping."
                    )
                    failed_extractions += 1
                    continue

                all_data = []
                current_start = earliest_ts
                end_time_ms = int(datetime.now().timestamp() * 1000)

                self.logger.info(
                    f"Extracting data for {symbol} from {ConvertDatetimeUtil.unix_ms_to_datetime(current_start)} to present"
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
                        f"Retrieved {len(data)} records for {symbol} up to {ConvertDatetimeUtil.unix_ms_to_datetime(last_time)}"
                    )

                    current_start = last_time + 1
                    time.sleep(0.3)

                    if len(data) < 1000:
                        break

                if not all_data:
                    self.logger.warning(f"No data extracted for {symbol}")
                    failed_extractions += 1
                    continue

                df = pd.DataFrame(all_data)
                df.drop_duplicates(subset=["fundingTime"], inplace=True)
                df["fundingTime"] = df["fundingTime"].apply(
                    ConvertDatetimeUtil.unix_ms_to_datetime
                )
                df = df.sort_values("fundingTime").reset_index(drop=True)
                df["symbol"] = symbol

                all_dataframes.append(df)
                successful_extractions += 1
                self.logger.info(
                    f"Successfully extracted {len(df)} records for {symbol}"
                )

                if i < len(symbols):
                    time.sleep(1)

            except Exception as e:
                failed_extractions += 1
                self.logger.error(f"Error extracting data for {symbol}: {str(e)}")
                continue

        self.logger.info(
            f"Extraction completed: {successful_extractions} successful, {failed_extractions} failed"
        )

        if successful_extractions > 0:
            combined_df = pd.concat(all_dataframes, ignore_index=True)
            combined_df = combined_df.sort_values(
                ["symbol", "fundingTime"]
            ).reset_index(drop=True)

            self.logger.info(
                f"Successfully extracted and combined funding rate data: {len(combined_df)} total records from {successful_extractions} symbols"
            )
            return combined_df
        else:
            self.logger.error("No data was successfully extracted for any symbol")
            return None
