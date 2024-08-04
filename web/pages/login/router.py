from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from utils import JSONBuildResponse
from pages.base import templates

router = APIRouter(
    prefix='/login',
    tags=['Pickup point']
)


@router.get('/')
async def login(
    request: Request, error: str = None
): 
    return templates.TemplateResponse(
        request=request, name="login.html", context={'error': error}
    )
