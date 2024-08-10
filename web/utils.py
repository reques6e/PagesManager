import json

class JSONBuildResponse:

    """
   
    Выдаёт Уже готовый json
   
    ---

    Разберём пример использования.
    ```py

    JSONBuildResponse(
        error=0,
        message='Всё ок'
    )
    ```

    В этом случае, error, это статус код задачи, 0 всё окей, ошибок в процессе выполнения задачи небыло, 1, ошибка процессе выполнения задачи.
   
    """

    def __init__(
        self, 
        error: int = 0, 
        message: str = 'Успех!', 
        **kwargs
    ) -> None:
        self.error = error
        self.message = message
        self.data = kwargs

    def json(
        self
    ):
        return {
            "error": self.error,
            "message": self.message,
            "data": self.data
        }
    

async def get_img_device(device_id: int):
    data = {
        (11091, 11087, 4154, 11094): 'https://tvip.tv/images/device/700%D1%85450_1.png',
        (11092, 11097): 'https://tvip.tv/images/device/700%D1%85450.png',
        (11077, 11078, 11085, 11079, 11080): 'https://thumb.tildacdn.com/tild6135-6538-4937-a439-633866326134/-/resize/42x/-/format/webp/1-11.png',
        (11111,): 'https://tvip.tv/images/device/705/700x450.png'
    }

    img_url = None
    for key_tuple, image_url in data.items():
        if device_id in key_tuple:
            img_url = image_url
            break

    if img_url:
        return img_url
    else:
        return 'https://tvip.tv/images/device/705/700x450.png'