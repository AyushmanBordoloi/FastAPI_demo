from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to my server"

products = [
    Product(pid=1, name="Phone", description="budget phone", price=99, quantity=10),
    Product(pid=2, name="Laptop", description="budget laptop", price=999, quantity=6),
    Product(pid=3, name="Headphones", description="budget headphones", price=49, quantity=15),
    Product(pid=4, name="Smartwatch", description="budget smartwatch", price=199, quantity=8),
]

@app.get("/products")
def get_all_products():
    return products