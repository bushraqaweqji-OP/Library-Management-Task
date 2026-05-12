from app.domain.books.entities import Book
from app.infrastructure.persistence.repositories.sqlalchemy_book_repository import BookRepository
from app.infrastructure.persistence.repositories.sqlalchemy_member_repository import MemberRepository
from app.shared.exceptions import (
    BookNotFoundException,
    MemberNotFoundException,
    BookNotBorrowedException
)


class BookService:

    @staticmethod
    def borrow_book(db, book_id, member_id):
        book = BookRepository.get_by_id(db, book_id)
        if not book:
            raise BookNotFoundException()

        member = MemberRepository.get_by_id(db, member_id)
        if not member:
            raise MemberNotFoundException()

        domain_book = Book(
            id=book.book_id,
            title=book.title,
            author=book.author,
            is_borrowed=book.is_borrowed,
            borrowed_by=book.borrowed_by,
            borrowed_date=book.borrowed_date,
        )
        domain_book.borrow(member_id)

        book.is_borrowed = domain_book.is_borrowed
        book.borrowed_by = domain_book.borrowed_by
        book.borrowed_date = domain_book.borrowed_date

        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def return_book(db, book_id, current_user):
        book = BookRepository.get_by_id(db, book_id)
        if not book:
            raise BookNotFoundException()

        if not book.is_borrowed:
            raise BookNotBorrowedException()

        domain_book = Book(
            id=book.book_id,
            title=book.title,
            author=book.author,
            is_borrowed=book.is_borrowed,
            borrowed_by=book.borrowed_by,
            borrowed_date=book.borrowed_date,
        )
        domain_book.return_book(current_user.member_id)

        book.is_borrowed = domain_book.is_borrowed
        book.borrowed_by = domain_book.borrowed_by
        book.borrowed_date = domain_book.borrowed_date

        db.commit()
        db.refresh(book)
        return book
