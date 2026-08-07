from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.dashboard_service import get_receipts
from app.database.database import engine

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/dashboard")
def dashboard(request: Request):

    if "user" not in request.session:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    with engine.connect():
        pass

    receipts = get_receipts()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "receipts": receipts
        }
    )