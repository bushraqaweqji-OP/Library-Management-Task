from sqlalchemy.orm import Session

from app.members.models import Member
from app.auth.security import (
    verify_password,
    create_access_token
)

def login_user(
    db: Session,
    email: str,
    password: str
):
    """Authenticate a user by their email and password, and return a JWT token if successful."""
    member = db.query(Member).filter(
        Member.email == email
    ).first()

    if not member:
        return None

    if not verify_password(
        password,
        member.password
    ):
        return None

    token = create_access_token(
        data={
            "sub": str(member.member_id)
        }
    )

    return token