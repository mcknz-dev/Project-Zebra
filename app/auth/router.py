from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.auth.client import supabase

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/health")
def auth_health():
    return {"status": "Authentication router working!"}


@router.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html"
    )


@router.post("/signup")
def signup(
    email: str = Form(...),
    password: str = Form(...)
):
    result = supabase.auth.sign_up({
        "email": email,
        "password": password,
    })

    print(result)

    return RedirectResponse(
        url="/auth/signup",
        status_code=303
    )


@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    result = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password,
    })

    # Store the logged in user in the session
    request.session["user_id"] = result.user.id
    request.session["email"] = result.user.email

    print(result)

    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )