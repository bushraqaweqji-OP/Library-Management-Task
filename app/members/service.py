from app.auth.security import hash_password
from app.core.exceptions import EmailAlreadyExistsException
from app.members.repository import MemberRepository


class MemberService:

    @staticmethod
    def create_member(db, member_data):

        """Service method to handle the logic for creating a new member record."""

        existing = MemberRepository.get_by_email(
            db,
            member_data.email
        )

        if existing:
            raise EmailAlreadyExistsException()

        data = member_data.dict()

        data["password"] = hash_password(
            data["password"]
        )

        return MemberRepository.create(
            db,
            data
        )