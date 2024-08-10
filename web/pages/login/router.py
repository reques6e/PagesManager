from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from web.utils import JSONBuildResponse
from web.pages.base import templates
from web.database import DataBase
from web.cores.session import SessionManager, SessionStorage
from web.cores.models.session import PayloadSession

db = DataBase()
storage = SessionStorage(name='session', secret='asdfdsfsdf')
session_manager = SessionManager(storage)

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


    lg = await db.auth_user_by_login_and_password(
        login=username, 
        password=password
    )
    print(lg) # (222, 'admin', 'root', '0', 1, 43534534, '192.168.0.0', '34534534534')

    if lg is None:
        request.session["error"] = "Invalid credentials"
        return RedirectResponse(url="/login", status_code=303)

    data = PayloadSession(
        user_id=lg[0],
        login=lg[1],
        password=lg[2],
        is_admin=lg[4],
        cookie_create_time=lg[5],
        ip=lg[6],
        token=lg[7]
    )
    session = await session_manager.create_session(data)

    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key='x-fastapicore-session', value=session)
    
    return response

