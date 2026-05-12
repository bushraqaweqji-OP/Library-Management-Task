from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.members.service import MemberService
from app.members.repository import MemberRepository
from typing import List


from app.shared.dependencies import get_db
from app.members.schemas import (
    CreateMember,
    MemberResponse,
    MemberUpdate
)

from app.core.exceptions import MemberNotFoundException

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)

@router.post("/", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
def create_member(
    member: CreateMember,
    db: Session = Depends(get_db)
):
    """
    Endpoint to create a new member record.
    """
    return MemberService.create_member(
        db,
        member
    )

@router.get("/", response_model=List[MemberResponse])
def get_members(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: str = None,
    db: Session = Depends(get_db)
):
    """
    Endpoint to retrieve all member records with optional search and pagination.
    """
    return MemberRepository.get_all(db, skip, limit, search)

@router.get("/{member_id}", response_model=MemberResponse)
def get_member(
    member_id: str,
    db: Session = Depends(get_db)
):
    """
    Endpoint to retrieve a member record by their ID.
    """
    member = MemberRepository.get_by_id(db, member_id)
    if not member:
        raise MemberNotFoundException()
    return member

@router.put("/{member_id}", response_model=MemberResponse)
def update_member(
    member_id: str,
    member_data: MemberUpdate,
    db: Session = Depends(get_db)
):
    """
    Endpoint to update a member record by their ID.
    """
    member = MemberRepository.get_by_id(db, member_id)
    if not member:
        raise MemberNotFoundException()

    for key, value in member_data.dict(exclude_unset=True).items():
        setattr(member, key, value)

    db.commit()
    db.refresh(member)

    return member

@router.delete("/{member_id}", response_model=MemberResponse)
def delete_member(
    member_id: str,
    db: Session = Depends(get_db)
):
    """
    Endpoint to delete a member record by their ID.
    """
    member = MemberRepository.delete(db, member_id)
    if not member:
        raise MemberNotFoundException()
    return member