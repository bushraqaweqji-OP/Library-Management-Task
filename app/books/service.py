from datetime import datetime, timezone
from http.client import HTTPException

from app.books.repository import BookRepository
from app.members.repository import MemberRepository

from app.core.exceptions import (
    BookNotBorrowedException,
    BookNotFoundException,
    MemberNotFoundException,
    BookAlreadyBorrowedException,
    WrongReturnBookException
)

class BookService:

    @staticmethod
    def borrow_book(db, book_id, member_id):
        """
        Service method to handle the logic for borrowing a book.
        """

        book = BookRepository.get_by_id(db, book_id)

        if not book:
            raise BookNotFoundException()

        member = MemberRepository.get_by_id(db, member_id)

        if not member:
            raise MemberNotFoundException()

        if book.is_borrowed:
            raise BookAlreadyBorrowedException()

        book.is_borrowed = True
        book.borrowed_by = member_id
        book.borrowed_date = datetime.now(timezone.utc)

        db.commit()
        db.refresh(book)

        return book

    @staticmethod
    def return_book(db, book_id, current_user):
        """
        Service method to handle the logic for returning a book.
        """

        book = BookRepository.get_by_id(db, book_id)

        if not book:
            raise BookNotFoundException()

        if not book.is_borrowed:
            raise BookNotBorrowedException()

        if book.borrowed_by != current_user.member_id:
            raise WrongReturnBookException()

        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_date = None

        db.commit()
        db.refresh(book)

        return book