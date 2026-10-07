class ExceptionValidation(Exception):
    """Custom exception class for validation errors."""

    def __init__(self, message):
        super().__init__(message)

    def validation_error(self, message):
        """Raise an exception for validation errors."""
        raise ExceptionValidation(f"Validation Error: {message}")
