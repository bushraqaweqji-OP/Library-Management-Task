from sqlalchemy.orm import Session
from app.members.models import Member

class MemberRepository:

    @staticmethod
    def create(db: Session, member_data):
        """
        Creates a new member record in the database.
        """
        member = Member(**member_data)
        db.add(member)
        db.commit()
        db.refresh(member)
        return member

    @staticmethod
    def get_by_email(db: Session, email: str):
        """
        Retrieves a member record by its email."""
        return db.query(Member).filter(
            Member.email == email
        ).first()

    @staticmethod
    def get_by_id(db: Session, member_id: str):
        """
        Retreieves a member record by its ID.
        """
        return db.query(Member).filter(
            Member.member_id == member_id
        ).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10, search: str = None):
        """
        Retrieves all member records from the database with optional search and pagination.
        """
        query = db.query(Member)
        if search:
            query = query.filter(Member.name.ilike(f"%{search}%"))
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def delete(db: Session, member_id: str):
        """
        Deletes a member record from the database by its ID.
        """
        member = db.query(Member).filter(
            Member.member_id == member_id
        ).first()

        if not member:
            return None

        db.delete(member)
        db.commit()
        return member