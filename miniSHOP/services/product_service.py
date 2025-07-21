from models import Product, ProductCreate
from typing import List, Optional
import db

def create_product(product_data: ProductCreate) -> Product:
    current_id = db.product_id_counter

    product_dict = {
        "id": current_id,
        "name": product_data.name,
        "stock": product_data.stock,
        "price": product_data.price
    }
    db.products.append(product_dict)
    db.product_id_counter += 1
    return Product(**product_dict)

def get_all_products() -> List[Product]:
    return [Product(**product_dict) for product_dict in db.products]

def get_product_by_id(product_id: int) -> Optional[Product]:
    for product_dict in db.products:
        if product_dict["id"] == product_id:
            return Product(**product_dict) 
    return None