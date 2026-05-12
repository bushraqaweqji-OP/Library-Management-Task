from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from app.core.database import Base

class Book(Base):
    """
    SQLAlchemy model for the Book entity.
    """
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    is_borrowed = Column(Boolean, default=False)
    borrowed_date = Column(DateTime, nullable=True)
    borrowed_by = Column(
        String, 
        ForeignKey("members.member_id"),
        nullable=True
    )


