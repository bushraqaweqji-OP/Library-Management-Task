from typing import Optional

from app.domain.books.services import BookService
from app.infrastructure.persistence.repositories.sqlalchemy_book_repository import BookRepository as SqlAlchemyBookRepository
from app.interfaces.schemas.books import BookCreate, BookUpdate


def create_book(db, book_data: BookCreate):
    return SqlAlchemyBookRepository.create(db, book_data)


def get_books(db, skip: int = 0, limit: int = 10, search: Optional[str] = None):
    return SqlAlchemyBookRepository.get_all(db, skip, limit, search)


def get_book(db, book_id: int):
    return SqlAlchemyBookRepository.get_by_id(db, book_id)


def update_book(db, book_id: int, book_data: BookUpdate):
    book = SqlAlchemyBookRepository.get_by_id(db, book_id)
    if not book:
        return None

    for key, value in book_data.dict(exclude_unset=True).items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


def borrow_book(db, book_id: int, member_id: str):
    return BookService.borrow_book(db, book_id, member_id)


def return_book(db, book_id: int, current_user):
    return BookService.return_book(db, book_id, current_user)
