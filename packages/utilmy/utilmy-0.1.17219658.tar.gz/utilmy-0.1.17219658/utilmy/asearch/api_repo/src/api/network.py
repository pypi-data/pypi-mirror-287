import aiohttp
import async_timeout

from conf import settings


async def make_request(
    url: str,
    method: str,
    data: dict = None,
    headers: dict = None
):
    """
    Args:
        url: is url for one of in-network services
        method: is lower version of one of HTTP methods: GET, POST, PUT, DELETE # noqa
        data: is payload
        headers: is header to put additional headers into request

    Returns:
        service result coming / non-blocking http request (coroutine)
        e.g:   {
                    "id": 2,
                    "username": "baranbartu",
                    "email": "baran@baran.com",
                    "full_name": "Baran Bartu Demirci",
                    "user_type": "baran",
                    "hashed_password": "***",
                    "created_by": 1
                }
    """
    if not data:
        data = {}

    with async_timeout.timeout(settings.GATEWAY_TIMEOUT):
        async with aiohttp.ClientSession() as session:
            request = getattr(session, method)
            async with request(url, json=data, headers=headers) as response:
                data = await response.json()
                return (data, response.status)
