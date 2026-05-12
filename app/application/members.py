from app.domain.members.services import MemberService
from app.infrastructure.persistence.repositories.sqlalchemy_member_repository import MemberRepository as SqlAlchemyMemberRepository
from app.interfaces.schemas.members import CreateMember


def create_member(db, member_data: CreateMember):
    return MemberService.create_member(db, member_data)


def get_members(db, skip: int = 0, limit: int = 10, search: str | None = None):
    return SqlAlchemyMemberRepository.get_all(db, skip, limit, search)


def get_member(db, member_id: str):
    return SqlAlchemyMemberRepository.get_by_id(db, member_id)


def update_member(db, member_id: str, member_data):
    member = SqlAlchemyMemberRepository.get_by_id(db, member_id)
    if not member:
        return None

    for key, value in member_data.dict(exclude_unset=True).items():
        setattr(member, key, value)

    db.commit()
    db.refresh(member)
    return member


def delete_member(db, member_id: str):
    return SqlAlchemyMemberRepository.delete(db, member_id)
