# Бета файл, его не нужно трогать
import sys
from pathlib import Path
import uvicorn

# Добавление пути к папке 'web' в sys.path
web_dir = Path(__file__).parent / 'web'
sys.path.insert(0, str(web_dir))

# Импорт web
import web.web as web_module

# Запуск сервера Uvicorn
if __name__ == "__main__":
    uvicorn.run(
        app='web.web:api', 
        host=web_module.Config.RUN_HOST, 
        port=web_module.Config.RUN_PORT,
        reload=web_module.Config.RUN_RELOAD
    )
