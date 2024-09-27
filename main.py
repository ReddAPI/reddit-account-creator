import configparser
import asyncio

from creator import create_account, client

config = configparser.ConfigParser()
config.read("config.ini")

API = config["ReddAPI"]["API_KEY"]
PROXY_PATH = config["DATA"]["PROXY_PATH"]

headers = {
    "x-rapidapi-key": API,
    "x-rapidapi-host": "reddapi.p.rapidapi.com",
    "Content-Type": "application/json"
}

def load_proxies():
    with open(PROXY_PATH, "r") as f:
        return f.read().split("\n")
    
proxies = load_proxies()
    
async def main():
    for proxy in proxies:
        response_data = await create_account(proxy, headers)
        print(response_data)


if __name__ == '__main__':
    asyncio.run(main())
    client.aclose()