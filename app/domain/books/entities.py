from datetime import datetime, timezone
from typing import Optional

from app.domain.books.exceptions import (
    BookAlreadyBorrowedException,
    BookNotBorrowedException,
    WrongReturnBookException,
)


class Book:

    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        is_borrowed: bool = False,
        borrowed_by: Optional[str] = None,
        borrowed_date: Optional[datetime] = None,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.borrowed_date = borrowed_date

    def borrow(self, member_id: str):
        if self.is_borrowed:
            raise BookAlreadyBorrowedException()

        self.is_borrowed = True
        self.borrowed_by = member_id
        self.borrowed_date = datetime.now(timezone.utc)

    def return_book(self, current_member_id: str):
        if not self.is_borrowed:
            raise BookNotBorrowedException()

        if self.borrowed_by != current_member_id:
            print(self.borrowed_by, type(self.borrowed_by))
            print(current_member_id, type(current_member_id))
            # raise WrongReturnBookException()

        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None