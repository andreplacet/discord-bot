import aiohttp

class HttpClient:
    def __init__(self):
        pass

    async def get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    json_response = await response.json()
                else:
                    json_response = False
        return json_response

    async def get_with_headers(self, url, headers):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    json_response = await response.json()
                else:
                    json_response = False
        return json_response