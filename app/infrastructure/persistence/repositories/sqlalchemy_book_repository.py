from sqlalchemy.orm import Session
from app.infrastructure.persistence.models.book_model import Book

class BookRepository:

    @staticmethod
    def create(db: Session, book_data):
        """
        Creates a new book record in the database.
        """
        book = Book(**book_data.dict())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10, search: str = None):
        """
        Retrieves all book records from the database with optional search and pagination.
        """
        query = db.query(Book)
        if search:
            query = query.filter(
                Book.title.ilike(f"%{search}%") | Book.author.ilike(f"%{search}%")
            )
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, book_id: int):
        """
        Retrieves a book record by its ID.
        """
        return db.query(Book).filter(
            Book.book_id == book_id
        ).first()
    

    @staticmethod
    def delete(db: Session, book):
        """
        Deletes a book record from the database.
        """
        db.delete(book)
        db.commit()