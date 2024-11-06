# app/schemas.py

from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str
    address: str
    created_at: str

class ProductCreate(BaseModel):
    name: str
    price: int
    quantity: int
    user_id: int

class BulkUserCreate(BaseModel):
    users: List[UserCreate]
