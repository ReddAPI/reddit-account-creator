import httpx

url = "https://reddapi.p.rapidapi.com/api/create_account"

client = httpx.AsyncClient(timeout=60, verify=False)

async def create_account(proxy:str, headers:dict):
    payload = { "proxy": proxy }
    response = await client.post(url, json=payload, headers=headers)
    return response.json()
