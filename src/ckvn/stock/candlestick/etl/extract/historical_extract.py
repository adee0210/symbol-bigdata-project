from pathlib import Path
from common.configs.logging_config import LoggingConfig


test = LoggingConfig.logging_config(
    "Test", Path("/home/duc/symbol-bigdata-project/logs")
)

test.info("xin chao")
