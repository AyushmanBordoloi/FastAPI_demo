from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to my server"

products = [
    Product(1, "Phone", "budget phone", 99, 10),
    Product(2, "Laptop", "budget laptop", 999, 6),
]

@app.get("/products")
def get_all_products():
    return products