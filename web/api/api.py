from fastapi import APIRouter
from web.api.user.router import router as user_api
from web.api.device.router import router as device_api
from web.utils import JSONBuildResponse

router = APIRouter(
    prefix='/api',
    tags=['Api']
)

@router.get("/")
async def api():
    return JSONBuildResponse(
        error=0,
        message='ByReques6e'
    )

router.include_router(user_api)
router.include_router(device_api)