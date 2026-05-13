from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.interfaces.dependencies import get_db, get_current_user
from app.interfaces.schemas.books import BookCreate, BookUpdate, BookResponse
from app.application.books import (
    create_book,
    get_books,
    get_book,
    update_book,
    borrow_book,
    return_book,
)
from app.domain.books.exceptions import BookNotFoundException


router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book_endpoint(
    book: BookCreate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Create a new book record.
    """
    return create_book(db, book)

@router.get("/", response_model=List[BookResponse])
def get_books_endpoint(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
    Retrieve all book records with optional search and pagination.
    """
    return get_books(db, skip, limit, search)

@router.get("/{book_id}", response_model=BookResponse)
def get_book_endpoint(
    book_id: int,
    db: Session = Depends(get_db),
):
    """
    Retrieve a book record by its ID.
    """
    book = get_book(db, book_id)
    if not book:
        raise BookNotFoundException()
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book_endpoint(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing book record.
    """
    book = update_book(db, book_id, book_data)
    if not book:
        raise BookNotFoundException()
    return book

@router.post("/borrow/{book_id}")
def borrow_book_endpoint(
    book_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Borrow a book by its ID.
    """
    return borrow_book(db, book_id, current_user.member_id)

@router.post("/return/{book_id}")
def return_book_endpoint(
    book_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    """
    Return a borrowed book.
    """
    return return_book(db, book_id, current_user)

