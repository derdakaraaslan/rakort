# app/main.py

from fastapi import FastAPI,  Depends
from sqlalchemy.orm import Session
from .crud.user import create_user, get_user, update_user, delete_user, bulk_insert_users, bulk_delete_users, bulk_update_users
from .crud.product import get_product, create_product, update_product, delete_product
from .schemas import UserCreate, BulkUserCreate, ProductCreate
from .database import get_db
from .utils import generate_random_string
from .models import User, Product
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

# region Users Apis
# ====================================================================
#  User API İşlemleri
# ====================================================================
@app.get("/users/")
def read_users(page: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    offset = (page - 1) * limit
    users = db.query(User).offset(offset).limit(limit).all()
    total_pages = (total_users // limit) + (1 if total_users % limit > 0 else 0)
    return {
        "page": page,
        "limit": limit,
        "total_users": total_users,
        "total_pages": total_pages,
        "users": users
    }

@app.get("/users/{user_id}")
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user(db=db, user_id=user_id)


@app.post("/users/")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.post("/random_bulk_insert_users/")
async def bulk_insert_users_endpoint(db: Session = Depends(get_db)):
    users_to_insert = []
    for _ in range(100000):
        user = {
            'name': generate_random_string(),
            'email': generate_random_string(12) + "@example.com",
            'address': generate_random_string(20),
            'created_at': '2024-11-06'
        }
        users_to_insert.append(user)
    bulk_insert_users(db=db, users_to_insert=users_to_insert)
    return {"message": "100.000 kullanıcı başarıyla eklendi!"}


@app.post("/bulk_insert_users/")
async def bulk_insert_users_by_data(data: BulkUserCreate, db: Session = Depends(get_db)):
    users_to_insert = []
    for user in data.users:
        users_to_insert.append({
            'name': user.name,
            'email': user.email,
            'address': user.address,
            'created_at': user.created_at
        })
    bulk_insert_users(db=db, users_to_insert=users_to_insert)
    return {"message": f"{len(users_to_insert)} kullanıcı başarıyla eklendi!"}


@app.put("/users/{user_id}")
def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user=user)


@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, user_id=user_id)

@app.delete("/random_bulk_delete_users/")
async def bulk_delete_users_endpoint(db: Session = Depends(get_db)):
    user_ids = [user.id for user in db.query(User).limit(100000).all()]
    return bulk_delete_users(db=db, user_ids=user_ids)


@app.delete("/bulk_delete_users/")
async def bulk_delete_users_endpoint(user_ids: list[int], db: Session = Depends(get_db)):
    return bulk_delete_users(db=db, user_ids=user_ids)


@app.put("/random_bulk_update_users/")
async def bulk_update_users_endpoint(db: Session = Depends(get_db)):
    user_ids = [user.id for user in db.query(User).limit(100000).all()]
    updated_data = {
        "name": "Updated Name",
    }
    return bulk_update_users(db=db, user_ids=user_ids, updated_data=updated_data)


@app.put("/bulk_update_users/")
async def bulk_update_users_endpoint(user_ids: list[int], updated_data: dict, db: Session = Depends(get_db)):
    return bulk_update_users(db=db, user_ids=user_ids, updated_data=updated_data)
# endregion

# region Product Apis
# ====================================================================
#  Product API İşlemleri
# ====================================================================

@app.get("/products/")
async def read_products(page: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    total_products = db.query(Product).count()
    offset = (page - 1) * limit
    products = db.query(Product).offset(offset).limit(limit).all()
    total_pages = (total_products // limit) + (1 if total_products % limit > 0 else 0)
    return {
        "page": page,
        "limit": limit,
        "total_products": total_products,
        "total_pages": total_pages,
        "products": products
    }


@app.get("/products/{product_id}")
async def read_product(product_id: int, db: Session = Depends(get_db)):
    return get_product(db=db, product_id=product_id)


@app.post("/products/")
async def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)


@app.put("/products/{product_id}")
async def update_product_endpoint(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    return update_product(db=db, product_id=product_id, product=product)


@app.delete("/products/{product_id}")
async def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db=db, product_id=product_id)

# endregion