# Бета файл, его не нужно трогать (говнокод)
import sys
import uvicorn
import asyncio

from pathlib import Path
from web import run as web_module
from web.database import DataBase

web_dir = Path(__file__).parent / 'web'
sys.path.insert(0, str(web_dir))

db = DataBase()

if __name__ == "__main__":
    asyncio.run(db.table_create())
    # asyncio.run(db.add_user(user_id=222, login='admin', password='root', _session='0', is_admin=1, cookie_create_time=43534534, ip='192.168.0.0', token='34534534534'))

    uvicorn.run(
        app='web.run:api', 
        host=web_module.Config.RUN_HOST, 
        port=web_module.Config.RUN_PORT,
        reload=web_module.Config.RUN_RELOAD
    )
