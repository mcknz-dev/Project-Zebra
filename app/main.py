from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

from app.routers import dashboard
from app.routers import uploads

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(dashboard.router)
app.include_router(uploads.router)