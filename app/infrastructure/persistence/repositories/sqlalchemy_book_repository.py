from sqlalchemy.orm import Session
from app.infrastructure.persistence.models.book_model import Book as BookModel
from app.domain.books.entities import Book as DomainBook

class BookRepository:

    @staticmethod
    def borrow(db: Session, book, member_id):
        """
        Handles the borrowing of a book by a member.
        """
        domain_book = DomainBook(
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
    def create(db: Session, book_data):
        """
        Creates a new book record in the database.
        """
        book = BookModel(**book_data.dict())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def delete(db: Session, book):
        """
        Deletes a book record from the database.
        """
        db.delete(book)
        db.commit()



    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10, search: str = None):
        """
        Retrieves all book records from the database with optional search and pagination.
        """
        query = db.query(BookModel)
        if search:
            query = query.filter(
                BookModel.title.ilike(f"%{search}%") | BookModel.author.ilike(f"%{search}%")
            )
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, book_id: int):
        """
        Retrieves a book record by its ID.
        """
        return db.query(BookModel).filter(
            BookModel.book_id == book_id
        ).first()
    
    @staticmethod
    def return_book(db: Session, book, member_id):
        """
        Handles the returning of a book by a member.
        """
        domain_book = DomainBook(
            id=book.book_id,
            title=book.title,
            author=book.author,
            is_borrowed=book.is_borrowed,
            borrowed_by=book.borrowed_by,
            borrowed_date=book.borrowed_date,
        )
        domain_book.return_book(member_id)

        book.is_borrowed = domain_book.is_borrowed
        book.borrowed_by = domain_book.borrowed_by
        book.borrowed_date = domain_book.borrowed_date

        db.commit()
        db.refresh(book)
        return book

    @staticmethod
    def update(db: Session, book, book_data):   
        """
        Updates an existing book record in the database.
        """
        for key, value in book_data.dict(exclude_unset=True).items():
            setattr(book, key, value)

        db.commit()
        db.refresh(book)
        return book

