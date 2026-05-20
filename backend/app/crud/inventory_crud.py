from sqlalchemy.orm import Session
from app.models.inventory import Inventory
import uuid


class InventoryCRUD:
    @staticmethod
    def get_inventory(db: Session, product_id: str):
        return db.query(Inventory).filter(Inventory.product_id == product_id).first()

    @staticmethod
    def get_all_inventory(db: Session):
        return db.query(Inventory).all()

    @staticmethod
    def get_low_stock_items(db: Session):
        return db.query(Inventory).filter(Inventory.quantity <= Inventory.reorder_level).all()

    @staticmethod
    def create_inventory(db: Session, product_id: str, quantity: int = 0, reorder_level: int = 10):
        db_inventory = Inventory(
            id=str(uuid.uuid4()),
            product_id=product_id,
            quantity=quantity,
            reorder_level=reorder_level
        )
        db.add(db_inventory)
        db.commit()
        db.refresh(db_inventory)
        return db_inventory

    @staticmethod
    def update_quantity(db: Session, product_id: str, quantity_change: int):
        db_inventory = InventoryCRUD.get_inventory(db, product_id)
        if db_inventory:
            db_inventory.quantity += quantity_change
            db.commit()
            db.refresh(db_inventory)
        return db_inventory

    @staticmethod
    def set_quantity(db: Session, product_id: str, quantity: int):
        db_inventory = InventoryCRUD.get_inventory(db, product_id)
        if db_inventory:
            db_inventory.quantity = quantity
            db.commit()
            db.refresh(db_inventory)
        return db_inventory

    @staticmethod
    def update_reorder_level(db: Session, product_id: str, reorder_level: int):
        db_inventory = InventoryCRUD.get_inventory(db, product_id)
        if db_inventory:
            db_inventory.reorder_level = reorder_level
            db.commit()
            db.refresh(db_inventory)
        return db_inventory
