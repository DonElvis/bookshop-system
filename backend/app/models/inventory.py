from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Inventory(Base):
    """Inventory tracking model."""
    __tablename__ = "inventory"

    id = Column(String, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), unique=True, index=True)
    quantity = Column(Integer, default=0)
    reorder_level = Column(Integer, default=10)
    last_restock_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    product = relationship("Product", back_populates="inventory")

    @property
    def needs_reorder(self) -> bool:
        """Check if inventory is below reorder level."""
        return self.quantity <= self.reorder_level

    def __repr__(self):
        return f"<Inventory(product_id={self.product_id}, quantity={self.quantity})>"
