import json

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from web.utils import JSONBuildResponse
from web.pages.base import templates
from web.cores.sdk.tms import TMS
from datetime import datetime

router = APIRouter(
    prefix='/dashboard',
    tags=['Dashboard']
)

tms = TMS(
    tms_url='http://tms.cyxym.net/api/admin',
    token=''
)

def format_timestamp(value):
    return datetime.fromtimestamp(value / 1000).strftime('%m.%d.%Y')

templates.env.filters['date'] = format_timestamp

@router.get("/")
async def dashboard(request: Request):
    find = request.query_params.get('find', None)
    if request.cookies.get('x-fastapicore-session') is None:
        return RedirectResponse(url="/login", status_code=303)

    json_data = await tms.get_all_devices(offset=0, limit=25, find=find)
    devices = json.loads(json_data['content'])['data']

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "json_data": {"data": devices}}
    )

@router.get("/device/{device_id}")
async def dashboard(request: Request, device_id: int):
    if request.cookies.get('x-fastapicore-session') is None:
        return RedirectResponse(url="/login", status_code=303)

    json_data = await tms.get_device_info(device_id=device_id)
    device = json.loads(json_data['content'])['data'][0]
    print(device)
    return templates.TemplateResponse(
        "device.html",
        {"request": request, "device": device}
    )


# @router.post("/oauth/check")
# async def handle_login(request: Request):
#     if request.cookies.get('x-fastapicore-session') == 'test':
#         return RedirectResponse(url="/dashboard", status_code=303)

#     form_data = await request.form()
#     username = form_data.get('username')
#     password = form_data.get('password')

#     if password != "root" or username != "admin":
#         request.session["error"] = "Invalid credentials"
#         return RedirectResponse(url="/login", status_code=303)

#     response = HTMLResponse(content="Login successful!")
#     response.set_cookie(key='x-fastapicore-session', value='test')

#     return response
