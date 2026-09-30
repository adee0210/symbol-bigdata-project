import logging


class LoggerUtil:
    @staticmethod
    def get_logger(name: str, level=logging.INFO):
        format = "%(asctime)s -%(name)s- %(levelname)s - %(message)s"
        formatter = logging.Formatter(format)
        RotatingFileHandler = logging.handlers.RotatingFileHandler(
            filename="logs/application.log",
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


test = LoggerUtil.get_logger("test", level=logging.INFO)
test.info("test")