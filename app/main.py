from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database.base import Base
from app.database.database import engine
from app.routers import receipts
from app.routers import dashboard
from app.routers import uploads
from app.routers import receipt
from app.auth import router as auth_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

Base.metadata.create_all(bind=engine)

app.include_router(dashboard.router)
app.include_router(uploads.router)
app.include_router(receipts.router)
app.include_router(receipt.router)
app.include_router(auth_router.router)