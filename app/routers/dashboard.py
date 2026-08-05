from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.dashboard_service import get_receipts
from app.database.database import engine

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def dashboard(request: Request):
    with engine.connect():
        pass

    receipts = get_receipts()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "receipts": receipts
        }
    )