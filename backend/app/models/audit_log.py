from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base


class AuditLog(Base):
    """Audit log model for tracking changes and compliance."""
    __tablename__ = "audit_logs"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    action = Column(String)
    resource_type = Column(String, index=True)
    resource_id = Column(String, index=True)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    def __repr__(self):
        return f"<AuditLog(id={self.id}, action={self.action}, resource_type={self.resource_type})>"
