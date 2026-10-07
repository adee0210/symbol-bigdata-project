import os
import threading

import oracledb
from dotenv import load_dotenv

from common.exception.exception_database import ExceptionDatabase

load_dotenv()


class DatabaseOracle:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize_pool()
        return cls._instance

    def _initialize_pool(self):
        self.username = os.getenv("ORACLE_USERNAME")
        self.password = os.getenv("ORACLE_PASSWORD")
        self.hostname = os.getenv("ORACLE_HOSTNAME")
        self.port = os.getenv("ORACLE_PORT")
        self.database = os.getenv("ORACLE_DATABASE")

        self.database_exception = ExceptionDatabase("Oracle database error")

        # Connection string (DSN)
        dsn = f"{self.hostname}:{self.port}/{self.database}"

        # Configure connection pool to avoid overloading the DB
        # This handles multiple concurrent connections efficiently
        try:
            self._pool = oracledb.create_pool(
                user=self.username,
                password=self.password,
                dsn=dsn,
                min=2,  # Minimum number of connections in the pool
                max=10,  # Maximum number of connections in the pool
                increment=1,  # Number of connections to add when the pool is exhausted
                getmode=oracledb.POOL_GETMODE_WAIT,  # Wait if all connections are in use
            )
            print("Oracle connection pool created successfully.")
        except oracledb.Error as e:
            self._pool = None
            raise self.database_exception.database_connection_error(
                f"Failed to create Oracle connection pool: {e}"
            )

    def get_connection(self):
        """Get a connection from the pool."""
        if self._pool is None:
            raise self.database_exception.database_connection_error(
                "Connection pool is not initialized."
            )
        return self._pool.acquire()

    def release_connection(self, connection):
        """Release the connection back to the pool."""
        if self._pool is not None and connection is not None:
            self._pool.release(connection)

    def close_pool(self):
        """Close the entire connection pool."""
        if self._pool is not None:
            self._pool.close()
            self._pool = None
            print("Oracle connection pool closed.")
