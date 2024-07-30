import dataclasses
import typing
from urllib.parse import urljoin
import requests
import aiohttp


@dataclasses.dataclass
class TPAuthData:
    auth: bool
    id: int
    token: str
    name: str
    alias: str
    email: str
    phone: str
    roles: typing.List[int]
    permissions: typing.List[int]


@dataclasses.dataclass
class TPAuthStatus:
    status: bool
    data: TPAuthData | None = None


class TJTPAuth:
    class Endpoint:
        LOGIN = '/api/user/login'
        FROM_TOKEN = '/api/user/fromtoken'

    def __init__(self, host: str):
        self._host = host
        self._login_endpoint = urljoin(self._host, self.Endpoint.LOGIN)
        self._from_token_endpoint = urljoin(self._host, self.Endpoint.FROM_TOKEN)

    @staticmethod
    def _create_auth_status(data: dict) -> TPAuthStatus:
        auth_data = TPAuthData(
            auth=data['auth'],
            id=data['id'],
            token=data['token'],
            name=data['name'],
            alias=data['alias'],
            email=data['email'],
            phone=data['phone'],
            roles=data['roles'],
            permissions=data['permissions']
        )
        return TPAuthStatus(status=True, data=auth_data)

    async def aio_from_token(self, token: str) -> TPAuthStatus:
        headers = {
            'accept': '*/*',
            'authorization': token
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self._from_token_endpoint, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._create_auth_status(data['data'])
                return TPAuthStatus(status=False, data=None)

    async def aio_login(self, username: str, password: str) -> TPAuthStatus:
        headers = {
            'accept': '*/*',
            'authorization': 'Bearer nothing here',
            'content-type': 'application/json',
        }
        payload = {
            'name': username,
            'password': password
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self._login_endpoint, headers=headers, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._create_auth_status(data['data'])
                return TPAuthStatus(status=False, data=None)

    def from_token(self, token: str) -> TPAuthStatus:
        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {token}'
        }
        response = requests.get(self._from_token_endpoint, headers=headers)
        if response.status_code == 200:
            return self._create_auth_status(response.json()['data'])
        return TPAuthStatus(status=False, data=None)

    def login(self, username: str, password: str) -> TPAuthStatus:
        headers = {
            'accept': '*/*',
            'authorization': 'Bearer nothing here',
            'content-type': 'application/json',
        }
        payload = {
            'name': username,
            'password': password
        }
        response = requests.post(self._login_endpoint, headers=headers, json=payload)
        if response.status_code == 200:
            return self._create_auth_status(response.json()['data'])
        return TPAuthStatus(status=False, data=None)
