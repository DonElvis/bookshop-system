from sqlalchemy.orm import Session
from app.models.order import Order, OrderItem, OrderStatus
from app.schemas.order import OrderCreateSchema
import uuid
from datetime import datetime


class OrderCRUD:
    @staticmethod
    def get_order(db: Session, order_id: str):
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def get_orders(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Order).offset(skip).limit(limit).all()

    @staticmethod
    def get_customer_orders(db: Session, customer_id: str):
        return db.query(Order).filter(Order.customer_id == customer_id).all()

    @staticmethod
    def get_orders_by_status(db: Session, status: str):
        return db.query(Order).filter(Order.status == status).all()

    @staticmethod
    def create_order(db: Session, order: OrderCreateSchema):
        # Calculate total
        total = 0
        for item in order.items:
            from app.models.product import Product
            product = db.query(Product).filter(Product.id == item.product_id).first()
            if product:
                total += product.price * item.quantity
        
        total -= order.discount_amount

        db_order = Order(
            id=str(uuid.uuid4()),
            customer_id=order.customer_id,
            total_amount=total,
            discount_amount=order.discount_amount,
            payment_method=order.payment_method,
            notes=order.notes,
            status=OrderStatus.PENDING
        )
        db.add(db_order)
        db.flush()

        for item in order.items:
            from app.models.product import Product
            product = db.query(Product).filter(Product.id == item.product_id).first()
            if product:
                order_item = OrderItem(
                    id=str(uuid.uuid4()),
                    order_id=db_order.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    unit_price=product.price
                )
                db.add(order_item)

        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def update_order_status(db: Session, order_id: str, status: str):
        db_order = OrderCRUD.get_order(db, order_id)
        if db_order:
            db_order.status = OrderStatus[status.upper()]
            db.commit()
            db.refresh(db_order)
        return db_order

    @staticmethod
    def cancel_order(db: Session, order_id: str):
        return OrderCRUD.update_order_status(db, order_id, "CANCELLED")
