from fastapi import FASTAPI
from routes.book_routes import router as book_router

app = FASTAPI(title = "library API")

app.include_router(book_router, prefix="/api")