import uuid
from sqlalchemy import Column, String
from app.core.database import Base


class Member(Base):
    """
    SQLAlchemy model for the Member entity.
    """
    __tablename__ = "members"

    member_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True,nullable=False, index=True)
    password = Column(String, nullable=True)

