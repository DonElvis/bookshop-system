from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreateSchema(BaseModel):
    """Schema for creating a new user."""
    username: str
    email: EmailStr
    password: str
    full_name: str
    role: str = "cashier"


class UserLoginSchema(BaseModel):
    """Schema for user login."""
    username: str
    password: str


class UserSchema(BaseModel):
    """Schema for user response."""
    id: str
    username: str
    email: str
    full_name: str
    role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
