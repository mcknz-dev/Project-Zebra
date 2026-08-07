from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.workspace_service import create_workspace

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/workspace/create")
def create_workspace_page(request: Request):
    print("SESSION:", request.session)

    return templates.TemplateResponse(
        request=request,
        name="create_workspace.html"
    )


@router.post("/workspace/create")
def create_workspace_route(
    request: Request,
    name: str = Form(...)
):
    create_workspace(
        user_id=request.session["user_id"],
        workspace_name=name,
    )
    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )