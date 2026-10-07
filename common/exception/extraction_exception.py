class ExtractionException(Exception):
    """Custom exception class for extraction errors."""

    def __init__(self, message):
        super().__init__(message)

    def extraction_connection_error(self, message):
        """Raise an exception for connection errors during extraction."""
        raise ExtractionException(f"Connection Error: {message}")

    def extraction_timeout_error(self, message):
        """Raise an exception for timeout errors during extraction."""
        raise ExtractionException(f"Timeout Error: {message}")

    def extraction_data_error(self, message):
        """Raise an exception for data errors during extraction."""
        raise ExtractionException(f"Data Error: {message}")

    def extraction_reponse_error(self, message):
        """Raise an exception for response errors during extraction."""
        raise ExtractionException(f"Response Error: {message}")

    def extraction_parsing_error(self, message):
        """Raise an exception for parsing errors during extraction."""
        raise ExtractionException(f"Parsing Error: {message}")

    def extraction_method_error(self, message):
        """Raise an exception for method errors during extraction."""
        raise ExtractionException(f"Method Error: {message}")
