from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import AppException

from app.interfaces.api.auth import router as auth_router
from app.interfaces.api.books import router as book_router
from app.interfaces.api.members import router as member_router

from app.domain.books.exceptions import (
    BookNotFoundException,
    BookAlreadyBorrowedException,
    WrongReturnBookException
)

from app.domain.members.exceptions import MemberNotFoundException

from app.domain.auth.exceptions import EmailAlreadyExistsException


app = FastAPI(
    title="Library Management System"
)

@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc: AppException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(BookNotFoundException)
async def book_not_found_handler(
    request: Request,
    exc: BookNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={"detail": "Book not found"}
    )


@app.exception_handler(MemberNotFoundException)
async def member_not_found_handler(
    request: Request,
    exc: MemberNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={"detail": "Member not found"}
    )


@app.exception_handler(EmailAlreadyExistsException)
async def email_exists_handler(
    request: Request,
    exc: EmailAlreadyExistsException
):
    return JSONResponse(
        status_code=400,
        content={"detail": "Email already exists"}
    )


@app.exception_handler(BookAlreadyBorrowedException)
async def borrowed_handler(
    request: Request,
    exc: BookAlreadyBorrowedException
):
    return JSONResponse(
        status_code=400,
        content={"detail": "Book already borrowed"}
    )


@app.exception_handler(WrongReturnBookException)
async def wrong_return_handler(
    request: Request,
    exc: WrongReturnBookException
):
    return JSONResponse(
        status_code=403,
        content={
            "detail": "Only the borrower can return this book"
        }
    )

app.include_router(book_router)
app.include_router(member_router)
app.include_router(auth_router)