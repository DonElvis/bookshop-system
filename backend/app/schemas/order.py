from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class OrderItemSchema(BaseModel):
    """Schema for order item."""
    id: str
    order_id: str
    product_id: str
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True


class OrderCreateItemSchema(BaseModel):
    """Schema for creating order item."""
    product_id: str
    quantity: int


class OrderSchema(BaseModel):
    """Schema for order/transaction."""
    id: str
    customer_id: Optional[str] = None
    total_amount: float
    discount_amount: float = 0
    payment_method: str
    status: str
    notes: Optional[str] = None
    items: List[OrderItemSchema] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OrderCreateSchema(BaseModel):
    """Schema for creating a new order."""
    customer_id: Optional[str] = None
    items: List[OrderCreateItemSchema]
    discount_amount: float = 0
    payment_method: str = "cash"
    notes: Optional[str] = None
