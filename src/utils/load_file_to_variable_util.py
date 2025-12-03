import glob
import json


class LoadFileToVariableUtil:
    @staticmethod
    def load_json_to_variable(filename, type):
        """
        Hàm tìm tên file và trả dữ liệu type dưới dạng DICT
        Input:
            - filename: tên file dạng json
            - type: trường dữ liệu muốn lấy ở đây bao gồm: vn_candle_stick_data,...
        Output:
            - Hàm trả ra DICT config theo type
        """
        file = glob.glob(f"**/{filename}", recursive=True)[0]
        with open(file=file, mode="r", encoding="utf-8") as f:
            return json.load(f)[type]
