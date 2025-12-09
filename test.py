import json
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import fs

hdfs = fs.HadoopFileSystem(host="localhost", port=9000, user="duc")

selector = fs.FileSelector("/user/duc_le", recursive=True)

info = hdfs.get_file_info(selector)

for info in info:
    print(f"Path:{info.path}")


with open("/home/duc/symbol-bigdata-project/data/2025-06-09 03:41:44.json", "r") as f:
    data = json.load(f)

table = pa.table(data)

with hdfs.open_output_stream(
    "/user/duc_le/data/symbol_data/vn/candlestick/etf/test.parquet"
) as file:
    pq.write_table(table, file)
