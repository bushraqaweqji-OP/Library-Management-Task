from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.infrastructure.persistence.database import SessionLocal
from app.infrastructure.persistence.repositories.sqlalchemy_member_repository import MemberRepository
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# Dependency function to get a database session for FastAPI routes and services.
def get_db():
    """
    Provides a database session for the duration of a request and ensures it is properly closed afterward.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        member_id = payload.get("sub")
        if member_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    member = MemberRepository.get_by_id(db, member_id)
    if member is None:
        raise credentials_exception

    return member
