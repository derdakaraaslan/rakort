# app/crud.py

from sqlalchemy.orm import Session
from ..models import User
from ..schemas import UserCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, address=user.address, created_at=user.created_at)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.address = user.address
        db_user.created_at = user.created_at
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def bulk_insert_users(db: Session, users_to_insert):
    db.bulk_insert_mappings(User, users_to_insert)
    db.commit()

def bulk_delete_users(db: Session, user_ids):
    db.query(User).filter(User.id.in_(user_ids)).delete(synchronize_session=False)
    db.commit()

def bulk_update_users(db: Session, user_ids, updated_data):
    db.query(User).filter(User.id.in_(user_ids)).update(updated_data, synchronize_session=False)
    db.commit()
