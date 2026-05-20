from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Customer(Base):
    """Customer model for customer management and loyalty."""
    __tablename__ = "customers"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    phone = Column(String, unique=True, index=True, nullable=True)
    loyalty_points = Column(Integer, default=0)
    total_spent = Column(String, default="0.00")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, loyalty_points={self.loyalty_points})>"
