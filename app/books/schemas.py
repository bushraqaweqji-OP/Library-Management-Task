from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BookCreate(BaseModel):
    """
    Pydantic model for creating a new book record.
    """
    title: str
    author : str

class BookUpdate(BaseModel):
    """
    Pydantic model for updating an existing book record.
    """
    title: Optional[str] = None
    author: Optional[str] = None

class BookResponse(BaseModel):
    """
    Pydantic model for retrieving a book record.
    """
    book_id: int
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime]
    borrowed_by: Optional[str]

    class Config:
        from_attributes = True