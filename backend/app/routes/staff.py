from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.staff_crud import StaffCRUD
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/staff", tags=["staff"])


class StaffSchema(BaseModel):
    id: str
    name: str
    email: str
    phone: str | None
    position: str
    shift: str
    hourly_rate: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class StaffCreateSchema(BaseModel):
    name: str
    email: str
    phone: str | None = None
    position: str
    shift: str = "morning"
    hourly_rate: str = "0.00"


@router.get("", response_model=List[StaffSchema])
async def get_staff(active_only: bool = False, db: Session = Depends(get_db)):
    """Get all staff members."""
    return StaffCRUD.get_all_staff(db, active_only=active_only)


@router.get("/{staff_id}", response_model=StaffSchema)
async def get_staff_member(staff_id: str, db: Session = Depends(get_db)):
    """Get a specific staff member."""
    staff = StaffCRUD.get_staff(db, staff_id)
    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found"
        )
    return staff


@router.post("", response_model=StaffSchema)
async def create_staff(staff: StaffCreateSchema, db: Session = Depends(get_db)):
    """Create a new staff member."""
    return StaffCRUD.create_staff(
        db,
        staff.name,
        staff.email,
        staff.position,
        staff.shift,
        staff.hourly_rate
    )


@router.put("/{staff_id}", response_model=StaffSchema)
async def update_staff(
    staff_id: str,
    staff_data: StaffCreateSchema,
    db: Session = Depends(get_db)
):
    """Update a staff member."""
    staff = StaffCRUD.update_staff(
        db,
        staff_id,
        staff_data.model_dump(exclude_unset=True)
    )
    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found"
        )
    return staff


@router.delete("/{staff_id}")
async def delete_staff(staff_id: str, db: Session = Depends(get_db)):
    """Deactivate a staff member."""
    staff = StaffCRUD.delete_staff(db, staff_id)
    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found"
        )
    return {"message": "Staff member deactivated"}
