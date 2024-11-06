# app/crud.py

from sqlalchemy.orm import Session
from ..models import  Product
from ..schemas import UserCreate, ProductCreate

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name, price=product.price, quantity=product.quantity, user_id=product.user_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

def bulk_insert_products(db: Session, products_to_insert):
    db.bulk_insert_mappings(Product, products_to_insert)
    db.commit()

def bulk_delete_products(db: Session, product_ids):
    db.query(Product).filter(Product.id.in_(product_ids)).delete(synchronize_session=False)
    db.commit()

def bulk_update_products(db: Session, product_ids, updated_data):
    db.query(Product).filter(Product.id.in_(product_ids)).update(updated_data, synchronize_session=False)
    db.commit()
