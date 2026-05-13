class AppException(Exception):
    """
    Base exception class for application-specific errors. All custom exceptions should inherit from this class.
    """
    status_code = 400
    detail = "Application error"
