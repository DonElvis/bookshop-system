from sqlalchemy.orm import Session
from app.models.product import Product, Category
from app.schemas.product import ProductCreateSchema
import uuid


class ProductCRUD:
    @staticmethod
    def get_product(db: Session, product_id: str):
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def get_products(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Product).offset(skip).limit(limit).all()

    @staticmethod
    def get_products_by_category(db: Session, category_id: str):
        return db.query(Product).filter(Product.category_id == category_id).all()

    @staticmethod
    def create_product(db: Session, product: ProductCreateSchema):
        db_product = Product(
            id=str(uuid.uuid4()),
            name=product.name,
            description=product.description,
            category_id=product.category_id,
            price=product.price,
            cost=product.cost,
            image_url=product.image_url
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def update_product(db: Session, product_id: str, product_data: dict):
        db_product = ProductCRUD.get_product(db, product_id)
        if db_product:
            for key, value in product_data.items():
                if hasattr(db_product, key) and value is not None:
                    setattr(db_product, key, value)
            db.commit()
            db.refresh(db_product)
        return db_product

    @staticmethod
    def delete_product(db: Session, product_id: str):
        db_product = ProductCRUD.get_product(db, product_id)
        if db_product:
            db.delete(db_product)
            db.commit()
        return db_product


class CategoryCRUD:
    @staticmethod
    def get_category(db: Session, category_id: str):
        return db.query(Category).filter(Category.id == category_id).first()

    @staticmethod
    def get_categories(db: Session):
        return db.query(Category).all()

    @staticmethod
    def create_category(db: Session, name: str, description: str = None):
        db_category = Category(
            id=str(uuid.uuid4()),
            name=name,
            description=description
        )
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category

    @staticmethod
    def update_category(db: Session, category_id: str, name: str = None, description: str = None):
        db_category = CategoryCRUD.get_category(db, category_id)
        if db_category:
            if name:
                db_category.name = name
            if description:
                db_category.description = description
            db.commit()
            db.refresh(db_category)
        return db_category

    @staticmethod
    def delete_category(db: Session, category_id: str):
        db_category = CategoryCRUD.get_category(db, category_id)
        if db_category:
            db.delete(db_category)
            db.commit()
        return db_category
