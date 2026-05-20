from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class OrderStatus(str, enum.Enum):
    """Order status enumeration."""
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PaymentMethod(str, enum.Enum):
    """Payment method enumeration."""
    CASH = "cash"
    CARD = "card"
    MOBILE_MONEY = "mobile_money"
    OTHER = "other"


class Order(Base):
    """Order/Transaction model for POS."""
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    customer_id = Column(String, ForeignKey("customers.id"), nullable=True, index=True)
    total_amount = Column(Float)
    discount_amount = Column(Float, default=0)
    payment_method = Column(Enum(PaymentMethod), default=PaymentMethod.CASH)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, index=True)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, total_amount={self.total_amount}, status={self.status})>"


class OrderItem(Base):
    """Order item model."""
    __tablename__ = "order_items"

    id = Column(String, primary_key=True, index=True)
    order_id = Column(String, ForeignKey("orders.id"), index=True)
    product_id = Column(String, ForeignKey("products.id"), index=True)
    quantity = Column(Integer)
    unit_price = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")

    @property
    def total(self) -> float:
        """Calculate total for this item."""
        return self.quantity * self.unit_price

    def __repr__(self):
        return f"<OrderItem(order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})>"
