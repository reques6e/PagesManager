import json

from fastapi import Request, APIRouter
from web.utils import JSONBuildResponse

router = APIRouter(
    prefix='/user',
    tags=['Dashboard']
)

    token = await db.get_user_info_by_token(token)
