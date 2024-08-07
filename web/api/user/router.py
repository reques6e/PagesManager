import json

from fastapi import Request, APIRouter
from web.utils import JSONBuildResponse

router = APIRouter(
    prefix='/user',
    tags=['Dashboard']
)

