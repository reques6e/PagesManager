from jwts import JWT
from config import Config
from models.session import GetSession

class SessionStorage:
    def __init__(
        self,
        name: str,
        secret: str = Config.JWT_SECRET
    ) -> None:
        self.name = name
        self.secret = secret


class SessionManager:
    def __init__(
        self,
        storage: SessionStorage
    ) -> None:
        self.storage = storage
        self._jwt = JWT(secret=storage.secret)

    async def get_session(
        self,
        _session: str,
    ) -> GetSession: 
        session = await self._jwt.encrypted(token=_session)

        # TODO: проверка валидности сесси 

        return GetSession(
            _session=session['_session'],
            user_id=session['user_id'],
            cookie_create_time=session['cookie_create_time'],
            ip=session['ip']
        )
    
    async def create_session(
        self,
        data: dict
    ) -> None: ...

    async def delete_session(
        self,
        _session: str
    ) -> None: ...
