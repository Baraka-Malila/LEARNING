from fastapi import FastAPI
from routes.products import router as products_router
from routes.sales import router as sales_router

app = FastAPI()

app.include_router(products_router)
app.include_router(sales_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
