from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.database.database import SessionLocal
from app.models.receipt import Receipt
from fastapi import HTTPException

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/receipts/{receipt_id}")
async def receipt_page(
    request: Request,
    receipt_id: int,
):

    db = SessionLocal()

    try:

        receipt = (
            db.query(Receipt)
            .filter(Receipt.id == receipt_id)
            .first()
        )

        if receipt is None:
            raise HTTPException(status_code=404, detail="Receipt not found")

    finally:

        db.close()

    return templates.TemplateResponse(
        request,
        "receipt.html",
        {
            "request": request,
            "receipt": receipt,
        },
    )