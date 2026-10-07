class DatabaseException(Exception):
    """Custom exception class for database errors."""

    def __init__(self, message):
        super().__init__(message)

    def database_connection_error(self, message):
        """Raise an exception for connection errors during database operations."""
        raise DatabaseException(f"Connection Error: {message}")

    def database_timeout_error(self, message):
        """Raise an exception for timeout errors during database operations."""
        raise DatabaseException(f"Timeout Error: {message}")

    def database_query_error(self, message):
        """Raise an exception for query errors during database operations."""
        raise DatabaseException(f"Query Error: {message}")

    def database_transaction_error(self, message):
        """Raise an exception for transaction errors during database operations."""
        raise DatabaseException(f"Transaction Error: {message}")
