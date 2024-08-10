import json

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from web.utils import JSONBuildResponse
from web.pages.base import templates
from web.tvip import tms
from datetime import datetime
from web.utils import get_img_device
router = APIRouter(
    prefix='/dashboard',
    tags=['Dashboard']
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
    device_types_data = await tms.get_device_types()
    
    devices = json_data['data']
    device_types = {d['id']: d['device_type'] for d in device_types_data['data']}

    for device in devices:
        device_type_id = device['device_type']
        device['image_url'] = await get_img_device(device_type_id)
        device['device_name'] = device_types.get(device_type_id, "Unknown")

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "json_data": {"data": devices}}
    )

@router.get("/device/{device_id}")
async def dashboard(request: Request, device_id: int):
    if request.cookies.get('x-fastapicore-session') is None:
        return RedirectResponse(url="/login", status_code=303)

    json_data = await tms.get_device(id=device_id)
    provider = await tms.get_provider(json_data['provider'])
    account = await tms.get_account(json_data['account'])

    device_type_id = json_data['device_type']
    json_data['image_url'] = await get_img_device(device_type_id)
    json_data['device_name'] = json_data.get(device_type_id, "Unknown")
    print(json_data)
    return templates.TemplateResponse(
        "device.html",
        {"request": request, "device": json_data, "provider": provider, "account": account}
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
