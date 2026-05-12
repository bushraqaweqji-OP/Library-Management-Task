from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List
from app.shared.dependencies import get_db
from app.books.schemas import BookCreate, BookUpdate, BookResponse
from app.books.repository import BookRepository
from app.books.service import BookService
from app.core.exceptions import BookNotFoundException
from app.auth.dependencies import get_current_user
from app.members.models import Member



router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreate,
    current_user: Member = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint to create a new book record.
    """
    return BookRepository.create(db, book)

@router.get("/", response_model=List[BookResponse])
def get_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: str = None,
    db: Session = Depends(get_db),
):
    """
    Endpoint to retrieve all book records with optional search and pagination."""
    return BookRepository.get_all(db, skip, limit, search)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    """
    Endpoint to retrieve a book record by its ID.
    """
    book = BookRepository.get_by_id(db, book_id)
    if not book:
        raise BookNotFoundException()
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db)
):
    """
    Endpoint to update a book record by its ID.
    """
    book = BookRepository.get_by_id(db, book_id)
    if not book:
        raise BookNotFoundException()

    # Update only the fields that are provided in the request
    for key, value in book_data.dict(exclude_unset=True).items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)

    return book

@router.post("/borrow/{book_id}")
def borrow_book(
    book_id: int,
    current_user: Member = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint to borrow a book by its ID and member ID.
    """
    return BookService.borrow_book(
        db,
        book_id,
        current_user.member_id
    )

@router.post("/return/{book_id}")
def return_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: Member = Depends(get_current_user)
):
    """Endpoint to return a book by its ID and member ID."""
    return BookService.return_book(
        db,
        book_id,
        current_user
    )

