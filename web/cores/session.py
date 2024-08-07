from jwts import JWT
from config import Config

from models.session import GetSession, PayloadSession

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
    ) -> PayloadSession:
        session = await self._jwt.encrypted(token=_session)

        # TODO: проверка валидности

        return PayloadSession(
            user_id=session['user_id'],
            cookie_create_time=session['cookie_create_time'],
            ip=session['ip']
        )

    async def create_session(
        self,
        data: PayloadSession
    ) -> GetSession:
        # TODO: проверка валидности

        payload = {
            '_session': data._session,
            'user_id': data.user_id,
            'cookie_create_time': data.cookie_create_time,
            'ip': data.ip
        }

        session = await self._jwt.crypted(payload=payload)

        return GetSession(
            _session=session,
            user_id=data.user_id,
            cookie_create_time=data.cookie_create_time,
            ip=data.ip
        )

    async def delete_session(
        self,
        _session: str
    ) -> None: ...
