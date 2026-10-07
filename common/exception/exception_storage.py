class ExceptionStorage(Exception):
    """Custom exception class for storage errors."""

    def __init__(self, message):
        super().__init__(message)

    def storage_connection_error(self, message):
        """Raise an exception for connection errors during storage operations."""
        raise ExceptionStorage(f"Connection Error: {message}")

    def storage_timeout_error(self, message):
        """Raise an exception for timeout errors during storage operations."""
        raise ExceptionStorage(f"Timeout Error: {message}")

    def storage_write_error(self, message):
        """Raise an exception for write errors during storage operations."""
        raise ExceptionStorage(f"Write Error: {message}")

    def storage_read_error(self, message):
        """Raise an exception for read errors during storage operations."""
        raise ExceptionStorage(f"Read Error: {message}")

    def storage_data_error(self, message):
        """Raise an exception for data errors during storage operations."""
        raise ExceptionStorage(f"Data Error: {message}")

    def storage_error(self, message):
        """Raise a general exception for storage errors."""
        raise ExceptionStorage(f"Storage Error: {message}")
