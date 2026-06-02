import logging
class Logger:
    @staticmethod
    def logger(log_name,log_level = logging.INFO):
        logger = logging.getLogger(log_name)
        logger.setLevel(log_level)
        file_handler = logging.FileHandler(log_name + '.log')
        file_handler.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger