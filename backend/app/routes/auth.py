from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreateSchema, UserLoginSchema, UserSchema
from app.crud.user_crud import UserCRUD
from app.auth.security import create_access_token
from datetime import timedelta
from app.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register(user: UserCreateSchema, db: Session = Depends(get_db)):
    """Register a new user."""
    existing_user = UserCRUD.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists"
        )
    
    existing_email = UserCRUD.get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )
    
    db_user = UserCRUD.create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password,
        full_name=user.full_name,
        role=user.role
    )
    
    return UserSchema.model_validate(db_user)


@router.post("/login")
async def login(credentials: UserLoginSchema, db: Session = Depends(get_db)):
    """Authenticate user and return access token."""
    user = UserCRUD.authenticate_user(db, credentials.username, credentials.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id, "username": user.username},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserSchema.model_validate(user)
    }
