import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


class LoggingConfig:
    @staticmethod
    def logging_config(log_name, log_path: Path, log_level=logging.INFO):
        log_path.mkdir(parents=True, exist_ok=True)
        log_file = log_path / "app.log"

        logger = logging.getLogger(name=log_name)
        logger.propagate = False
        logger.setLevel(log_level)
        if logger.handlers:
            return logger

        # formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(processName)s - %(levelname)s - %(name)s - %(message)s"
        )

        # handlers
        file_handler = RotatingFileHandler(
            filename=log_file, maxBytes=5 * 1024 * 1024, backupCount=5
        )

        console_handler = logging.StreamHandler()

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        return logger
