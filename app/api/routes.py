from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.crud import product as crud

router = APIRouter()

@router.post("/products", response_model=ProductOut)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/products", response_model=list[ProductOut])
def list_all(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.get("/products/{product_id}", response_model=ProductOut)
def get(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=ProductOut)
def update(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    product = crud.update_product(db, product_id, product_data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}
