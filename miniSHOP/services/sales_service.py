from models import Sales, SalesCreate, SalesTotal
from typing import List, Optional
from services.product_service import get_product_by_id
from datetime import datetime
import db

def create_sale(product_id: int, sale_data: SalesCreate) -> Sales:
    product = get_product_by_id(product_id)
    
    if product is None:
        raise ValueError("Product not found")
    
    if product.stock < sale_data.quantity:
        raise ValueError("Insufficient stock")
    
    total_price = product.price * sale_data.quantity
    
    current_id = db.sale_id_counter
    sale_dict = {
        "id": current_id,
        "product_id": product_id,
        "quantity": sale_data.quantity,
        "total_price": total_price,
        "timestamp": datetime.now()
    }
    
    db.sales.append(sale_dict)
    db.sale_id_counter += 1
    
    for product_dict in db.products:
        if product_dict["id"] == product_id:
            product_dict["stock"] -= sale_data.quantity
            break
    
    return Sales(**sale_dict)

def get_sales_total() -> SalesTotal:
    total_sales = sum(sale_dict["total_price"] for sale_dict in db.sales)
    
    total_transactions = len(db.sales)
    
    return SalesTotal(
        total_sales=total_sales,
        total_transactions=total_transactions
    )