import json
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)

import datetime
import requests
from configs.logger_config import LoggerConfig
from configs.variable_config import CMC_CONFIG
from src.utils.convert_content_file_to_variable_util import (
    ConvertContentFileToVariableUtil,
)
from src.utils.convert_datetime_util import ConvertDatetimeUtil


class CMCHistoricalExtract:
    def __init__(self) -> None:
        self.logger = LoggerConfig.logger_config("CMCHistoricalExtract")
        self.cmc_historical_url = CMC_CONFIG["cmc_historical_url"]
        self.cmc_historical_time_end = CMC_CONFIG["cmc_historical_time_end"]
        self.cmc_historical_day = CMC_CONFIG["cmc_historical_day"]
        self.cmc_symbol_id = ConvertContentFileToVariableUtil.get_top100_symbol_id()

    def get_data_from_requests(self, time_start, time_end, id):
        """
        INPUT:
            - time_start (str) dang unixtime theo giay: Thoi diem bat dau
            - time_end (str) dang unixtime theo giay: Thoi diem ket thuc
            - id (int): id cua symbol tren Coin Market Cap

        OUTPUT:
            - JSON: Tra ve data cho cac tham so tren
        """
        try:
            self.logger.info(
                f"Send requests to {self.cmc_historical_url} with timeStart:{ConvertDatetimeUtil.unix_second_to_datetime(time_start)} and timeEnd: {ConvertDatetimeUtil.unix_second_to_datetime(time_end)}"
            )
            response = requests.get(
                url=self.cmc_historical_url.replace("symbol_id", str(id))
                .replace("symbol_time_start", str(time_start))
                .replace("symbol_time_end", str(time_end)),
                timeout=30,
            )
            data = response.json()["data"]["quotes"]
            return data

        except Exception as e:
            self.logger.error(f"Error to send request: {(str(e))}")
            return None

    def extract(self):
        """
        THUAT TOAN:
            - Chia thanh n luong moi luong thuc hien 1 task
            - Moi lan chi duoc lay toi da 400 ban ghi
            - Task: endtime = unixtime now, startime = unixtime(thoi gian ban ghi cu nhat) => endtime = startime, startime = unixtime(ban ghi cu nhat).... la dau vao cho get_data_from_request()
            - Den khi khong con data thi stop

        """
        self.logger.info("Starting to extract CMC historical data ...")
        day_to_second = self.cmc_historical_day * 86400
        time_end = int(datetime.datetime.now().timestamp())

        for i in range(len(self.cmc_symbol_id)):
            while True:
                try:
                    time_start = time_end - day_to_second
                    id = self.cmc_symbol_id[i]
                    data_from_request = self.get_data_from_requests(
                        time_start=time_start, time_end=time_end, id=id
                    )
                    if len(data_from_request["data"]["quotes"]) == 0:
                        self.logger.warning("khong co data trong khoang thoi gian nay")
                        break

                    time_end = ConvertDatetimeUtil.iso_to_unix_ms(
                        data_from_request[0]["quote"]["timestamp"]
                    )

                except Exception as e:
                    self.logger.error(
                        f"Error to extract CMC historical data Error: {(str(e))}"
                    )
