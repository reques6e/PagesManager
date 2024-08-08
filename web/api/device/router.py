from fastapi import APIRouter
from fastapi.responses import JSONResponse
from web.utils import JSONBuildResponse
from web.tvip import tms


router = APIRouter(
    prefix='/device',
    tags=['Api']
)

@router.post("/reboot")
async def device_reboot(
    device_id: int
):
    rs = await tms.send_command(
        device_id=device_id,
        command='RestartCommand',\
        command_name='restart'
    )

    if rs['error'] == 'Unexpected content type':
        return JSONResponse(
            content=JSONBuildResponse(
                error=0,
                message='Запрос на перезапуск был успешно отправлен',
                device_id=device_id
            ).json(),
            status_code=200
        )
    else:
        return JSONResponse(
            content=JSONBuildResponse(
                error=1,
                message='На сервере произошла ошибка',
                error_json=rs
            ).json(),
            status_code=500
        )  
     
@router.post("/app")
async def device_app_start(
    device_id: int,
    app: str
):
    rs = await tms.send_command(
        device_id=device_id,
        application=app,
        command='StartApplicationCommand',\
        command_name='start_application'
    )

    if rs['error'] == 'Unexpected content type':
        return JSONResponse(
            content=JSONBuildResponse(
                error=0,
                message=f'Запрос на запуск {app} был успешно отправлен',
                device_id=device_id
            ).json(),
            status_code=200
        )
    else:
        return JSONResponse(
            content=JSONBuildResponse(
                error=1,
                message='На сервере произошла ошибка',
                error_json=rs
            ).json(),
            status_code=500
        )   