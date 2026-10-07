import logging
import logging.handlers
import os


class LoggingLogger:
    @staticmethod
    def get_logger(name: str, filename: str, level=logging.INFO):
        format = "%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(format)
    
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        RotatingFileHandler = logging.handlers.RotatingFileHandler(
            filename=f"logs/{filename}.log",
            maxBytes=1024 * 1024 * 10,
            backupCount=5,
        )
        RotatingFileHandler.setLevel(level)
        RotatingFileHandler.setFormatter(formatter)

        for handler in logging.getLogger(name).handlers:
            logging.getLogger(name).removeHandler(handler)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(RotatingFileHandler)
        return logger

    @staticmethod
    def remove_all_handlers(logger: logging.Logger):
        for handler in logger.handlers:
            logger.removeHandler(handler)
