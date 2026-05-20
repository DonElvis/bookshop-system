from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CategorySchema(BaseModel):
    """Schema for product category."""
    id: str
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class ProductSchema(BaseModel):
    """Schema for product/snack."""
    id: str
    name: str
    description: Optional[str] = None
    category_id: str
    price: float
    cost: float
    image_url: Optional[str] = None
    is_active: int = 1
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductCreateSchema(BaseModel):
    """Schema for creating a new product."""
    name: str
    description: Optional[str] = None
    category_id: str
    price: float
    cost: float
    image_url: Optional[str] = None
