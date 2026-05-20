from sqlalchemy import Column, String, DateTime, Boolean, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum


class ShiftType(str, enum.Enum):
    """Shift type enumeration."""
    MORNING = "morning"
    AFTERNOON = "afternoon"
    NIGHT = "night"
    FULL_DAY = "full_day"


class Staff(Base):
    """Staff/Employee model."""
    __tablename__ = "staff"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    position = Column(String)
    shift = Column(Enum(ShiftType), default=ShiftType.MORNING)
    hourly_rate = Column(String, default="0.00")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Staff(id={self.id}, name={self.name}, position={self.position})>"
