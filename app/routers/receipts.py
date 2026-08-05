from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.database.database import SessionLocal
from app.models.receipt import Receipt

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/receipts")
async def receipts_page(request: Request):

    db = SessionLocal()

    try:

        receipts = db.query(Receipt).all()

    finally:

        db.close()

    return templates.TemplateResponse(
        request,
        "receipts.html",
        {
            "request": request,
            "receipts": receipts,
        },
    )