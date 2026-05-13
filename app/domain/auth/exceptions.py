from app.core.exceptions import AppException


class EmailAlreadyExistsException(AppException):
    """
    Exception raised when an email address is already registered.
    """
    status_code = 400
    detail = "Email already exists"

class InvalidCredentialsException(AppException):
    """
    Exception raised when user authentication fails due to invalid credentials.
    """
    status_code = 401
    detail = "Invalid email or password"