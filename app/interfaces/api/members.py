from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List
from app.interfaces.dependencies import get_db
from app.interfaces.schemas.members import (
    CreateMember,
    MemberResponse,
    MemberUpdate,
)
from app.application.members import (
    create_member,
    get_members,
    get_member,
    update_member,
    delete_member,
)
from app.shared.exceptions import MemberNotFoundException

router = APIRouter(
    prefix="/members",
    tags=["Members"],
)

@router.post("/", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
def create_member_endpoint(
    member: CreateMember,
    db: Session = Depends(get_db),
):
    """
    Create a new member record.
    """
    return create_member(db, member)

@router.get("/", response_model=List[MemberResponse])
def get_members_endpoint(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    db: Session = Depends(get_db),
):
    """
    Retrieve all member records with optional search and pagination.
    """
    return get_members(db, skip, limit, search)

@router.get("/{member_id}", response_model=MemberResponse)
def get_member_endpoint(
    member_id: str,
    db: Session = Depends(get_db),
):
    """
    Retrieve a member record by their ID.
    """
    member = get_member(db, member_id)
    if not member:
        raise MemberNotFoundException()
    return member

@router.put("/{member_id}", response_model=MemberResponse)
def update_member_endpoint(
    member_id: str,
    member_data: MemberUpdate,
    db: Session = Depends(get_db),
):
    """
    Update a member record by their ID.
    """
    member = update_member(db, member_id, member_data)
    if not member:
        raise MemberNotFoundException()
    return member

@router.delete("/{member_id}", response_model=MemberResponse)
def delete_member_endpoint(
    member_id: str,
    db: Session = Depends(get_db),
):
    """
    Delete a member record by their ID.
    """
    member = delete_member(db, member_id)
    if not member:
        raise MemberNotFoundException()
    return member
