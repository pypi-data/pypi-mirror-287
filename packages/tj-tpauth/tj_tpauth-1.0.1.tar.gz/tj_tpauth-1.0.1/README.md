# TJ-TPAuth 1.0.0

### Sync

```python
from tj_tpauth import TJTPAuth

tpauth = TJTPAuth(
    host='http://localhost:3000'
)

login_status = tpauth.login(
    username='username',
    password='password'
)

if not login_status.status:
    exit(0)

auth_status = tpauth.from_token(login_status.data.token)

if not login_status.status:
    exit(0)

print(auth_status.data)
```

### Async

```python
import asyncio

from tj_tpauth import TJTPAuth

tpauth = TJTPAuth(
    host='http://localhost:3000'
)


async def main():
    login_status = await tpauth.aio_login(
        username='username',
        password='password'
    )

    if not login_status.status:
        exit(0)

    auth_status = await tpauth.aio_from_token(login_status.data.token)

    if not login_status.status:
        exit(0)

    print(auth_status.data)


asyncio.run(main())
```