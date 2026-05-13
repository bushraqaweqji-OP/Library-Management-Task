from app.domain.books.entities import Book
from app.infrastructure.persistence.repositories.sqlalchemy_book_repository import BookRepository
from app.infrastructure.persistence.repositories.sqlalchemy_member_repository import MemberRepository
from app.domain.books.exceptions import (
    BookNotFoundException,
    BookNotBorrowedException
)

from app.domain.members.exceptions import MemberNotFoundException

class BookService:

    @staticmethod
    def borrow_book(db, book_id, member_id):
        book = BookRepository.get_by_id(db, book_id)
        if not book:
            raise BookNotFoundException()

        member = MemberRepository.get_by_id(db, member_id)
        if not member:
            raise MemberNotFoundException()

        return BookRepository.borrow(db, book, member_id)

    @staticmethod
    def return_book(db, book_id, current_user):
        book = BookRepository.get_by_id(db, book_id)
        if not book:
            raise BookNotFoundException()

        if not book.is_borrowed:
            raise BookNotBorrowedException()

        return BookRepository.return_book(db, book, current_user)

    @staticmethod
    def update_book(db, book_id, book_data):
        book = BookRepository.get_by_id(db, book_id)
        if not book:
            return None

        if book.is_borrowed:
            raise Exception("Cannot edit borrowed book")

        return BookRepository.update(db, book, book_data)