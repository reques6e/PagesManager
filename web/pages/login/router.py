from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from web.utils import JSONBuildResponse
from web.pages.base import templates

router = APIRouter(
    prefix='/login',
    tags=['Login (oauth)']
)

@router.get('/')
async def login(
    request: Request, 
    error: str = None
): 
    if request.cookies.get('x-fastapicore-session') == 'test':
        return RedirectResponse(url="/dashboard", status_code=303)

    error = request.session.get("error")
    if error:
        del request.session["error"]

    return templates.TemplateResponse(
        request=request, name="login.html", context={'error': error}
    )

@router.post("/oauth/check")
async def handle_login(request: Request):
    if request.cookies.get('x-fastapicore-session') == 'test':
        return RedirectResponse(url="/dashboard", status_code=303)

    form_data = await request.form()
    username = form_data.get('username')
    password = form_data.get('password')

    if password != "root" or username != "admin":
        request.session["error"] = "Invalid credentials"
        return RedirectResponse(url="/login", status_code=303)

    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key='x-fastapicore-session', value='test')
    
    return response

