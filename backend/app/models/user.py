from sqlalchemy import Column, String, DateTime, Boolean, Enum
from sqlalchemy.sql import func
from datetime import datetime
from app.database import Base
import enum


class UserRole(str, enum.Enum):
    """User roles in the system."""
    ADMIN = "admin"
    MANAGER = "manager"
    CASHIER = "cashier"
    INVENTORY_STAFF = "inventory_staff"


class User(Base):
    """User model for authentication and authorization."""
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CASHIER)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, role={self.role})>"
