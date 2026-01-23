import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


class LoggingConfig:
    @staticmethod
    def logging_config(log_name, log_dir: Path, log_level: int = logging.INFO):
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "main.log"

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
        file_handlers = RotatingFileHandler(
            filename=log_file, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
        )

        console_handlers = logging.StreamHandler()

        file_handlers.setFormatter(formatter)
        console_handlers.setFormatter(formatter)

        logger.addHandler(console_handlers)
        logger.addHandler(file_handlers)

        return logger
