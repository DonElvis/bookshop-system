from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderSchema, OrderCreateSchema
from app.crud.order_crud import OrderCRUD
from typing import List

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("", response_model=List[OrderSchema])
async def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all orders."""
    return OrderCRUD.get_orders(db, skip=skip, limit=limit)


@router.get("/{order_id}", response_model=OrderSchema)
async def get_order(order_id: str, db: Session = Depends(get_db)):
    """Get a specific order."""
    order = OrderCRUD.get_order(db, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order


@router.post("", response_model=OrderSchema)
async def create_order(order: OrderCreateSchema, db: Session = Depends(get_db)):
    """Create a new order (POS transaction)."""
    return OrderCRUD.create_order(db, order)


@router.patch("/{order_id}/status")
async def update_order_status(
    order_id: str,
    status: str,
    db: Session = Depends(get_db)
):
    """Update order status."""
    order = OrderCRUD.update_order_status(db, order_id, status)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order


@router.patch("/{order_id}/cancel")
async def cancel_order(order_id: str, db: Session = Depends(get_db)):
    """Cancel an order."""
    order = OrderCRUD.cancel_order(db, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return {"message": "Order cancelled", "order": order}
