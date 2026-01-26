import json

from common.utils.convert_datetime_util import ConvertDatetimeUtil

with open("test.json", "r") as f:
    data = json.load(f)

print(ConvertDatetimeUtil.unix_second_to_datetime_utc(data["t"][0]))
