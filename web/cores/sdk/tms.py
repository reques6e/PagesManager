import json
import aiohttp
import io
import time

from typing import Optional, Dict, AnyStr

class TMS:
    def __init__(self, tms_url: str, token: str) -> None:
        self.tms_url = tms_url
        self.token = token

    async def _request(self, page: str, data: Optional[Dict] = None, type_: str = 'GET') -> dict:
        headers = {
            'Authorization': f'Basic {self.token}',
            'Content-Type': 'application/json'
        }

        async with aiohttp.ClientSession() as session:
            async with session.request(method=type_, url=f'{self.tms_url}/{page}', json=data, headers=headers) as response:
                if response.status in (200, 401):
                    content_type = response.headers.get('Content-Type', '')
                    if 'application/json' in content_type:
                        return await response.json()
                    else:
                        return {"error": "Unexpected content type", "content": await response.text()}
                else:
                    return {"error": f"Unexpected status code: {response.status}", "content": await response.text()}

    async def get_all_devices(
        self, 
        offset: int, 
        limit: int, 
        find: Optional[str] = None
    ) -> dict:
        query_find = f'quick_search={find}' if find else ''

        return await self._request(
            page=f'devices/?start={offset}&limit={limit}&{query_find}',
            data={},
            type_='GET'
        )

    async def get_device(
        self, 
        id: int
    ) -> dict:
        return await self._request(
            page=f'devices/{id}',
            data={},
            type_='GET'
        )
    
    async def get_provider(
        self, 
        id: int
    ) -> dict:
        return await self._request(
            page=f'providers/{id}',
            data={},
            type_='GET'
        )

    async def get_account(
        self, 
        id: int
    ) -> dict:
        return await self._request(
            page=f'accounts/{id}',
            data={},
            type_='GET'
        )

    async def get_device_types(
        self
    ) -> dict:
        return await self._request(
            page=f'device_types?start=0&limit=250',
            data={},
            type_='GET'
        )
    
    async def get_device_info(
        self, 
        device_id: int
    ) -> dict:
        return await self._request(
            page=f'command/?start=0&limit=25&filter=deviceId;=;{device_id}',
            data={},
            type_='GET'
        )

    async def send_command(
        self, 
        device_id: int, 
        application: str = None,
        command: str = None, 
        command_name: str = None
    ) -> dict:
        # RestartCommand - перезапуск приставки
        ## commandName - restart
        # navigator - браузер (StartApplicationCommand)
        ## commandName - start_application

        return await self._request(
            page=f'command/devices/',
            data={
                "ids":[device_id],
                "commands":[
                    {
                        "id": None,
                        "@class": f"com.tviplabs.tms.api.admin.general.model.command.{command}",
                        "commandName": command_name,
                        "created": int(time.time()),
                        "postTime": None,
                        "ttl": None,
                        "@id": "2",
                        "application": application
                    }
                ],
                "@id":"1"
            },
            type_='POST'
        )