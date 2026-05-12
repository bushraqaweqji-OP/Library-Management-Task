from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.shared.dependencies import get_db
from app.auth.schemas import TokenResponse
from app.auth.service import login_user
from app.core.exceptions import InvalidCredentialsException

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Endpoint to authenticate a user and return a JWT token."""
    token = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:
        raise InvalidCredentialsException()

    return {
        "access_token": token,
        "token_type": "bearer"
    }