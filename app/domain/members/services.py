from app.infrastructure.persistence.repositories.sqlalchemy_member_repository import MemberRepository
from app.infrastructure.security import hash_password
from app.shared.exceptions import EmailAlreadyExistsException


class MemberService:

    @staticmethod
    def create_member(db, member_data):
        existing = MemberRepository.get_by_email(db, member_data.email)
        if existing:
            raise EmailAlreadyExistsException()

        data = member_data.dict()
        data["password"] = hash_password(data["password"])
        return MemberRepository.create(db, data)
