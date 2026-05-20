from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.product import ProductSchema, ProductCreateSchema, CategorySchema
from app.crud.product_crud import ProductCRUD, CategoryCRUD
from typing import List
import uuid

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/categories", response_model=List[CategorySchema])
async def get_categories(db: Session = Depends(get_db)):
    """Get all product categories."""
    return CategoryCRUD.get_categories(db)


@router.post("/categories", response_model=CategorySchema)
async def create_category(
    name: str,
    description: str = None,
    db: Session = Depends(get_db)
):
    """Create a new category."""
    return CategoryCRUD.create_category(db, name, description)


@router.get("", response_model=List[ProductSchema])
async def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all products."""
    return ProductCRUD.get_products(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: str, db: Session = Depends(get_db)):
    """Get a specific product."""
    product = ProductCRUD.get_product(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product


@router.post("", response_model=ProductSchema)
async def create_product(product: ProductCreateSchema, db: Session = Depends(get_db)):
    """Create a new product."""
    return ProductCRUD.create_product(db, product)


@router.put("/{product_id}", response_model=ProductSchema)
async def update_product(
    product_id: str,
    product_data: ProductCreateSchema,
    db: Session = Depends(get_db)
):
    """Update a product."""
    product = ProductCRUD.update_product(
        db,
        product_id,
        product_data.model_dump(exclude_unset=True)
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product


@router.delete("/{product_id}")
async def delete_product(product_id: str, db: Session = Depends(get_db)):
    """Delete a product."""
    product = ProductCRUD.delete_product(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return {"message": "Product deleted successfully"}
