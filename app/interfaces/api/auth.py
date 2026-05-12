from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.interfaces.dependencies import get_db
from app.interfaces.schemas.auth import TokenResponse
from app.application.auth import authenticate_user
from app.shared.exceptions import InvalidCredentialsException

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """Endpoint to authenticate a user and return a JWT token."""
    token = authenticate_user(
        db,
        form_data.username,
        form_data.password,
    )

    if not token:
        raise InvalidCredentialsException()

    return {
        "access_token": token,
        "token_type": "bearer",
    }
