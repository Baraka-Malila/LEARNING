from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    id: int
    name:str
    stock: int
    price: float

class ProductCreate(BaseModel):
    name: str
    stock: int
    price: float

class Sales(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    timestamp: datetime

class SalesCreate(BaseModel):
    quantity: int

class SalesTotal(BaseModel):
    total_sales: float
    total_transactions: int