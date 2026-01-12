from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


class LoggingConfig:
    @staticmethod
    def logging_config(log_name, log_dir: Path, log_level=logging.INFO):
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "main.log"

        logger = logging.getLogger(name=log_name)
        logger.setLevel(log_level)
        logger.propagate = False

        if logger.handlers:
            return logger
        # forrmatter
        formatter = logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(name)s - %(message)s")

        # handlers
        file_handler = RotatingFileHandler(filename=log_file,maxBytes=5*1024*1024,backupCount=5,encoding="utf-8")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
