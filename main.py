from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to my server"

products = [
    Product(pid=1, name="Phone", description="budget phone", price=99, quantity=10),
    Product(pid=2, name="Laptop", description="budget laptop", price=999, quantity=6),
    Product(pid=5, name="Headphones", description="budget headphones", price=49, quantity=15),
    Product(pid=6, name="Smartwatch", description="budget smartwatch", price=199, quantity=8),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.pid == id:
            return product
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