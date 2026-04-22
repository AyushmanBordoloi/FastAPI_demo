from pydantic import BaseModel

class Product(BaseModel):
    pid: int
    name: str
    description: str
    price: float
    quantity: int
