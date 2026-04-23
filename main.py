from fastapi import Depends, FastAPI
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to my server"

products = [
    Product(pid=1, name="Phone", description="budget phone", price=99, quantity=10),
    Product(pid=2, name="Laptop", description="budget laptop", price=999, quantity=6),
    Product(pid=5, name="Headphones", description="budget headphones", price=49, quantity=15),
    Product(pid=6, name="Smartwatch", description="budget smartwatch", price=199, quantity=8),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.pid == id).first()
    if db_product:
        return db_product
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].pid == id:
            products[i] = product
            return "Product Added successfully"
    return "Product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].pid == id:
            del products[i]
            return "Product deleted successfully"
    return "Product not found"