from sqlalchemy.orm import Session
from app.models.user import User, UserRole
from app.auth.security import hash_password, verify_password
import uuid


class UserCRUD:
    @staticmethod
    def get_user(db: Session, user_id: str):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def create_user(db: Session, username: str, email: str, password: str, full_name: str, role: str = "cashier"):
        db_user = User(
            id=str(uuid.uuid4()),
            username=username,
            email=email,
            hashed_password=hash_password(password),
            full_name=full_name,
            role=UserRole[role.upper()],
            is_active=True
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def authenticate_user(db: Session, username: str, password: str):
        db_user = UserCRUD.get_user_by_username(db, username)
        if db_user and verify_password(password, db_user.hashed_password):
            return db_user
        return None

    @staticmethod
    def update_user(db: Session, user_id: str, user_data: dict):
        db_user = UserCRUD.get_user(db, user_id)
        if db_user:
            for key, value in user_data.items():
                if hasattr(db_user, key) and value is not None:
                    if key == "password":
                        value = hash_password(value)
                        key = "hashed_password"
                    if key == "role":
                        value = UserRole[value.upper()]
                    setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: str):
        db_user = UserCRUD.get_user(db, user_id)
        if db_user:
            db_user.is_active = False
            db.commit()
            db.refresh(db_user)
        return db_user
