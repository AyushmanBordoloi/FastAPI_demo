from pydantic import BaseModel

class Product:
    pid: int
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, pid: int, name: str, description: str, price: float, quantity: int):
        self.pid = pid
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity