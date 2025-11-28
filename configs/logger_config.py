import logging
from logging.handlers import RotatingFileHandler
import os


class LoggerConfig:
    """
    Cấu hình logger cho từng module/file, mỗi logger ghi ra file riêng biệt.
    """

    @staticmethod
    def get_logger(name, log_file, level=logging.INFO):
        """
        Tạo logger ghi ra file riêng biệt trong thư mục logs/.
        name: tên logger (thường là __name__)
        log_file: tên file log (ví dụ: 'module_a.log')
        level: cấp độ log
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.handlers.clear()  # Xóa các handler cũ để tránh ghi trùng

        # Đảm bảo thư mục logs/ tồn tại
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir = os.path.join(project_root, "logs")
        os.makedirs(logs_dir, exist_ok=True)
        log_path = os.path.join(logs_dir, log_file)

        handler = RotatingFileHandler(
            log_path, maxBytes=10 * 1024 * 1024, backupCount=3, encoding="utf-8"
        )
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        )
        logger.addHandler(handler)
        logger.propagate = False
        return logger
