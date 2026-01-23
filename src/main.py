from pathlib import Path

from common.configs.logging_config import LoggingConfig


path = Path("/home/duc/symbol-bigdata-project/logs")
test = LoggingConfig.logging_config(log_name="test", log_dir=path)
test.info("xin chao bo may test cai code nay")
