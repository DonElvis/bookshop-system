from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.product import ProductCreateSchema
from app.crud.inventory_crud import InventoryCRUD
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/inventory", tags=["inventory"])


class InventorySchema(BaseModel):
    id: str
    product_id: str
    quantity: int
    reorder_level: int
    needs_reorder: bool

    class Config:
        from_attributes = True


@router.get("", response_model=List[InventorySchema])
async def get_inventory(db: Session = Depends(get_db)):
    """Get all inventory."""
    return InventoryCRUD.get_all_inventory(db)


@router.get("/low-stock", response_model=List[InventorySchema])
async def get_low_stock_items(db: Session = Depends(get_db)):
    """Get items below reorder level."""
    return InventoryCRUD.get_low_stock_items(db)


@router.get("/{product_id}", response_model=InventorySchema)
async def get_product_inventory(product_id: str, db: Session = Depends(get_db)):
    """Get inventory for a specific product."""
    inventory = InventoryCRUD.get_inventory(db, product_id)
    if not inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory not found"
        )
    return inventory


@router.patch("/{product_id}/quantity")
async def update_quantity(
    product_id: str,
    quantity_change: int,
    db: Session = Depends(get_db)
):
    """Update inventory quantity (add/subtract)."""
    inventory = InventoryCRUD.update_quantity(db, product_id, quantity_change)
    if not inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory not found"
        )
    return inventory


@router.patch("/{product_id}/reorder-level")
async def update_reorder_level(
    product_id: str,
    reorder_level: int,
    db: Session = Depends(get_db)
):
    """Update reorder level."""
    inventory = InventoryCRUD.update_reorder_level(db, product_id, reorder_level)
    if not inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory not found"
        )
    return inventory
