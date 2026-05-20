from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.customer_crud import CustomerCRUD
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/customers", tags=["customers"])


class CustomerSchema(BaseModel):
    id: str
    name: str
    email: str | None
    phone: str | None
    loyalty_points: int
    total_spent: str
    created_at: datetime

    class Config:
        from_attributes = True


class CustomerCreateSchema(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None


@router.get("", response_model=List[CustomerSchema])
async def get_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all customers."""
    return CustomerCRUD.get_customers(db, skip=skip, limit=limit)


@router.get("/{customer_id}", response_model=CustomerSchema)
async def get_customer(customer_id: str, db: Session = Depends(get_db)):
    """Get a specific customer."""
    customer = CustomerCRUD.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer


@router.post("", response_model=CustomerSchema)
async def create_customer(customer: CustomerCreateSchema, db: Session = Depends(get_db)):
    """Create a new customer."""
    return CustomerCRUD.create_customer(db, customer.name, customer.email, customer.phone)


@router.put("/{customer_id}", response_model=CustomerSchema)
async def update_customer(
    customer_id: str,
    customer_data: CustomerCreateSchema,
    db: Session = Depends(get_db)
):
    """Update a customer."""
    customer = CustomerCRUD.update_customer(
        db,
        customer_id,
        customer_data.model_dump(exclude_unset=True)
    )
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer


@router.patch("/{customer_id}/loyalty-points")
async def add_loyalty_points(
    customer_id: str,
    points: int,
    db: Session = Depends(get_db)
):
    """Add loyalty points to customer."""
    customer = CustomerCRUD.add_loyalty_points(db, customer_id, points)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer


@router.delete("/{customer_id}")
async def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    """Delete a customer."""
    customer = CustomerCRUD.delete_customer(db, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return {"message": "Customer deleted"}
