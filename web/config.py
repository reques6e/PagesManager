

class Config:

    """
    Конфиг.

    В него не нужно вписывать всё что подлежит обновлению со стороны API, для этого есть json-ы.
        
    """

    RUN_HOST = '0.0.0.0'
    RUN_PORT = 5000
    RUN_RELOAD = True

    JWT_SECRET = 'kjasdhasdjsa'
    JWT_HASH = 'HS256'

    class DataBase:
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'test',
            'password': '7255777',
            'db': 'test'
        }

    