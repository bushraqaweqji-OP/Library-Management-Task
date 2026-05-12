class AppException(Exception):
    """
    Base exception class for application-specific errors. All custom exceptions should inherit from this class.
    """
    status_code = 400
    detail = "Application error"


class BookNotFoundException(AppException):
    """
    Exception raised when a book record is not found in the database.
    """
    status_code = 404
    detail = "Book not found"


class MemberNotFoundException(AppException):
    """
    Exception raised when a member record is not found in the database.
    """
    status_code = 404
    detail = "Member not found"


class BookAlreadyBorrowedException(AppException):
    """
    Exception raised when a book is already borrowed.
    """
    status_code = 400
    detail = "Book already borrowed"

class BookNotBorrowedException(AppException):
    """
    Exception raised when trying to return a book that is not currently borrowed.
    """
    status_code = 400
    detail = "Book is not currently borrowed"

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

class WrongReturnBookException(AppException):
    """
    Exception raised when a member tries to return a book that they did not borrow.
    """
    status_code = 403
    detail = "You cannot return a book borrowed by another member"