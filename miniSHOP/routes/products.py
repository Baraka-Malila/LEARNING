from fastapi import APIRouter, HTTPException
from models import Product, ProductCreate
from services.product_service import create_product, get_all_products
from typing import List

router = APIRouter()

@router.post("/products", response_model=Product)
def add_product(product_data: ProductCreate) -> Product:
    """
    Create a new product.
    Takes ProductCreate data and returns Product with ID.
    """
    try:
        new_product = create_product(product_data)
        return new_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/products", response_model=List[Product])
def list_products() -> List[Product]:
    try:
        products = get_all_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
