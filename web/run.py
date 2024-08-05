import asyncio
import subprocess
import uvicorn
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from pages.exceptions import FastAPIExceptionHandlers
from pages.login.router import router as page_login

from config import Config

def compile_scss():
    try:
        print(os.getcwd())
        result = subprocess.run(['bash', 'scripts/compile_scss.sh'], check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении скрипта: {e}")
        print(e.stderr)


api = FastAPI(
    title='By Reques6e',
    version='0.1.0',
    redoc_url=None,
    description='TestLOL'
)

api.add_middleware(SessionMiddleware, secret_key='your-secret-key')
api.mount("/static", StaticFiles(directory="web/ui/static"), name="static")

FastAPIExceptionHandlers(api)

api.include_router(page_login)

compile_scss()

if __name__ == "__main__":
    uvicorn.run(
        app='run:api', 
        host=Config.RUN_HOST, 
        port=Config.RUN_PORT,
        reload=Config.RUN_RELOAD
    )
