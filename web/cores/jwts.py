import jwt
import asyncio


class JWT:
    def __init__(self, secret: str) -> None:
        self.secret = secret

    async def crypted(self, payload: dict) -> str:
        """
        Пример использования
        
        ```py

        jwt_instance = JWT(secret='test')

        async def main():
            token = await jwt_instance.crypted({'test': 'test'})
            return token

        print(asyncio.run(main()))

        ```
        """
        return jwt.encode(payload=payload, key=self.secret, algorithm='HS256')

    async def encrypted(self, token: str) -> dict:
        """
        Пример использования

        ```py
        jwt_instance = JWT(secret='test')

        async def main():
            decoded = await jwt_instance.encrypted(token)
            return decoded

        token = asyncio.run(main())
        print(token)
        ```
        """

        try:
            return jwt.decode(token, key=self.secret, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")

