from fastapi import FastAPI

from app.books.routes import router as book_router
from app.members.routes import router as member_router
from app.core.database import engine, Base
from app.books.models import Book
from app.members.models import Member
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import AppException
from app.auth.routes import router as auth_router


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

app.include_router(book_router)
app.include_router(member_router)
app.include_router(auth_router)