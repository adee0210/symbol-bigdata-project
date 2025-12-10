from pyarrow import fs
from configs.config_env import HDFS_CONFIG


class PyarrowUtil:
    def __init__(self):
        self.hdfs_host = HDFS_CONFIG["hdfs_host"]
        self.hdfs_port = HDFS_CONFIG["hdfs_port"]
        self.hdfs_user = HDFS_CONFIG["hdfs_user"]

    def hdfs(self):
        hdfs = fs.HadoopFileSystem(
            host=self.hdfs_host, port=self.hdfs_port, user=self.hdfs_user
        )
        return hdfs
