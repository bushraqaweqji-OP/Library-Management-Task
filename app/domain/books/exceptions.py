from app.core.exceptions import AppException


class BookNotFoundException(AppException):
    """
    Exception raised when a book record is not found in the database.
    """
    status_code = 404
    detail = "Book not found"

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

class WrongReturnBookException(AppException):
    """
    Exception raised when a member tries to return a book that they did not borrow.
    """
    status_code = 403
    detail = "You cannot return a book borrowed by another member"