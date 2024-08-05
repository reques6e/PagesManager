# Бета файл, его не нужно трогать (говнокод)
import sys
import uvicorn

from pathlib import Path
from web import run as web_module

web_dir = Path(__file__).parent / 'web'
sys.path.insert(0, str(web_dir))


if __name__ == "__main__":
    uvicorn.run(
        app='web.run:api', 
        host=web_module.Config.RUN_HOST, 
        port=web_module.Config.RUN_PORT,
        reload=web_module.Config.RUN_RELOAD
    )
