from sqlalchemy.orm import Session
from app.infrastructure.persistence.repositories.sqlalchemy_member_repository import MemberRepository
from app.infrastructure.security import verify_password, create_access_token


def login_user(
    db: Session,
    email: str,
    password: str,
):
    """Authenticate a user by their email and password and return a JWT token."""
    member = MemberRepository.get_by_email(db, email)
    if not member:
        return None

    if not verify_password(password, member.password):
        return None

    return create_access_token({"sub": str(member.member_id)})
