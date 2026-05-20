from sqlalchemy.orm import Session
from app.models.customer import Customer
import uuid


class CustomerCRUD:
    @staticmethod
    def get_customer(db: Session, customer_id: str):
        return db.query(Customer).filter(Customer.id == customer_id).first()

    @staticmethod
    def get_customers(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Customer).offset(skip).limit(limit).all()

    @staticmethod
    def get_customer_by_email(db: Session, email: str):
        return db.query(Customer).filter(Customer.email == email).first()

    @staticmethod
    def get_customer_by_phone(db: Session, phone: str):
        return db.query(Customer).filter(Customer.phone == phone).first()

    @staticmethod
    def create_customer(db: Session, name: str, email: str = None, phone: str = None):
        db_customer = Customer(
            id=str(uuid.uuid4()),
            name=name,
            email=email,
            phone=phone,
            loyalty_points=0,
            total_spent="0.00"
        )
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer

    @staticmethod
    def update_customer(db: Session, customer_id: str, customer_data: dict):
        db_customer = CustomerCRUD.get_customer(db, customer_id)
        if db_customer:
            for key, value in customer_data.items():
                if hasattr(db_customer, key) and value is not None:
                    setattr(db_customer, key, value)
            db.commit()
            db.refresh(db_customer)
        return db_customer

    @staticmethod
    def add_loyalty_points(db: Session, customer_id: str, points: int):
        db_customer = CustomerCRUD.get_customer(db, customer_id)
        if db_customer:
            db_customer.loyalty_points += points
            db.commit()
            db.refresh(db_customer)
        return db_customer

    @staticmethod
    def delete_customer(db: Session, customer_id: str):
        db_customer = CustomerCRUD.get_customer(db, customer_id)
        if db_customer:
            db.delete(db_customer)
            db.commit()
        return db_customer
