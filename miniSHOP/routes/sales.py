from fastapi import APIRouter, HTTPException
from models import Sales, SalesCreate, SalesTotal
from services.sales_service import create_sale, get_sales_total

router = APIRouter()

@router.post("/sales/{product_id}", response_model=Sales)
def sell_product(product_id: int, sale_data: SalesCreate) -> Sales:
    try:
        new_sale = create_sale(product_id, sale_data)
        return new_sale
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sales/total", response_model=SalesTotal)
def get_total_sales() -> SalesTotal:
    try:
        sales_summary = get_sales_total()
        return sales_summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
