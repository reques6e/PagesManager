from web.cores.jwts import JWT
from web.config import Config

from web.cores.models.session import GetSession, PayloadSession
from web.database import DataBase


db = DataBase()


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
            login=session['login'],
            password=session['password'],
            is_admin=session['is_admin'],
            cookie_create_time=session['cookie_create_time'],
            ip=session['ip'],
            token=session['token']
        )

    async def create_session(
        self,
        data: PayloadSession
    ) -> str:
        payload = {
            'user_id': data.user_id,
            'login': data.login,
            'password': data.password,
            'is_admin': data.is_admin,
            'cookie_create_time': data.cookie_create_time,
            'ip': data.ip,
            'token': data.token
        }

        session = await self._jwt.crypted(payload=payload)

        await db.add_session(
            user_id=data.user_id,
            _session=session,
            cookie_create_time=data.cookie_create_time,
            ip=data.ip
        )

        return session

    async def delete_session(
        self,
        _session: str
    ) -> None: ...
