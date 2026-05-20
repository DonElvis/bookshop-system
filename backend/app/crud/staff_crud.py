from sqlalchemy.orm import Session
from app.models.staff import Staff, ShiftType
import uuid


class StaffCRUD:
    @staticmethod
    def get_staff(db: Session, staff_id: str):
        return db.query(Staff).filter(Staff.id == staff_id).first()

    @staticmethod
    def get_all_staff(db: Session, active_only: bool = False):
        query = db.query(Staff)
        if active_only:
            query = query.filter(Staff.is_active == True)
        return query.all()

    @staticmethod
    def get_staff_by_email(db: Session, email: str):
        return db.query(Staff).filter(Staff.email == email).first()

    @staticmethod
    def create_staff(db: Session, name: str, email: str, position: str, shift: str = "morning", hourly_rate: str = "0.00"):
        db_staff = Staff(
            id=str(uuid.uuid4()),
            name=name,
            email=email,
            position=position,
            shift=ShiftType[shift.upper()],
            hourly_rate=hourly_rate,
            is_active=True
        )
        db.add(db_staff)
        db.commit()
        db.refresh(db_staff)
        return db_staff

    @staticmethod
    def update_staff(db: Session, staff_id: str, staff_data: dict):
        db_staff = StaffCRUD.get_staff(db, staff_id)
        if db_staff:
            for key, value in staff_data.items():
                if hasattr(db_staff, key) and value is not None:
                    if key == "shift" and value:
                        value = ShiftType[value.upper()]
                    setattr(db_staff, key, value)
            db.commit()
            db.refresh(db_staff)
        return db_staff

    @staticmethod
    def delete_staff(db: Session, staff_id: str):
        db_staff = StaffCRUD.get_staff(db, staff_id)
        if db_staff:
            db_staff.is_active = False
            db.commit()
            db.refresh(db_staff)
        return db_staff
