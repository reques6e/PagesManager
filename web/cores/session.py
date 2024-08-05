from models.session import GetSession
from jwts import JWT

class SessionStorage:
    def __init__(
        self,
        name: str,
        secret: str,
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


if __name__ == '__main__':
    storage = SessionStorage(
        name='start',
        secret='test'
    )

    manager = SessionManager(
        storage=storage
    )

    import asyncio

    async def main(): 
        _storage = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfc2Vzc2lvbiI6InRlc3QiLCJ1c2VyX2lkIjoxMjM0LCJjb29raWVfY3JlYXRlX3RpbWUiOjQ0NDQ0LCJpcCI6IjE5Mi4xNjguMC4xMDAifQ.1l7VNkgc5g0GiuOm1ejhOaQP6z3KUhmxC5cxNRbYLgg'
        rs = await manager.get_session(_storage)
        print(rs)

    asyncio.run(main())