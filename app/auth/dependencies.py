from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.shared.dependencies import get_db
from app.core.config import settings
from app.members.repository import MemberRepository


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """Dependency to get the current authenticated user based on the JWT token provided in the request."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        member_id = payload.get("sub")

        if member_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    member = MemberRepository.get_by_id(
        db,
        member_id
    )

    if member is None:
        raise credentials_exception

    return member