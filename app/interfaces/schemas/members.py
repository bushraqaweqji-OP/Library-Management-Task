from typing import Optional
from pydantic import BaseModel, EmailStr


class CreateMember(BaseModel):
    """
    Pydantic model for creating a new member record.
    """
    name: str
    email: EmailStr
    password: str

class MemberUpdate(BaseModel):
    """
    Pydantic model for updating an existing member record.
    """
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class MemberResponse(BaseModel):
    """
    Pydantic model for retrieving a member record.
    """
    member_id: str
    name: str
    email: EmailStr

    class Config:
        from_attributes = True