import aiomysql

from web.config import Config


class DataBase:
    def __init__(self) -> None:
        self.db_config = Config.DataBase.db_config

    async def table_create(self):
        pool = await aiomysql.create_pool(**self.db_config)

        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users(
                        user_id BIGINT PRIMARY KEY,
                        _session TEXT,
                        is_admin INTEGER,
                        cookie_create_time INTEGER,
                        ip TEXT,
                        token TEXT
                    )
                ''')
                await conn.commit()

                await cursor.execute('''
                    CREATE TABLE IF NOT EXISTS favorites(
                        user_id BIGINT PRIMARY KEY,
                        cams TEXT
                    )
                ''')
                await conn.commit()

        pool.close()
        await pool.wait_closed()

    async def get_user_info_by_id(self, user_id: int):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
                    return await cursor.fetchone()

    async def get_user_info_by_token(self, token: str):
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("SELECT * FROM users WHERE token = %s", (token,))
                    return await cursor.fetchone()                