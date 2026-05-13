from app.core.exceptions import AppException


class MemberNotFoundException(AppException):
    """
    Exception raised when a member record is not found in the database.
    """
    status_code = 404
    detail = "Member not found"

