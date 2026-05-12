class AppException(Exception):
    """
    Base exception class for application-specific errors.
    """
    status_code = 400
    detail = "Application error"


class BookNotFoundException(AppException):
    status_code = 404
    detail = "Book not found"


class MemberNotFoundException(AppException):
    status_code = 404
    detail = "Member not found"


class BookAlreadyBorrowedException(AppException):
    status_code = 400
    detail = "Book already borrowed"


class BookNotBorrowedException(AppException):
    status_code = 400
    detail = "Book is not currently borrowed"


class EmailAlreadyExistsException(AppException):
    status_code = 400
    detail = "Email already exists"


class InvalidCredentialsException(AppException):
    status_code = 401
    detail = "Invalid email or password"


class WrongReturnBookException(AppException):
    status_code = 403
    detail = "You cannot return a book borrowed by another member"
