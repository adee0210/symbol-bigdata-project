import os


class GetPathUtil:
    @staticmethod
    def get_root_path():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_data_raw_path():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, "../.."))
        return os.path.join(project_root, "data", "raw")
