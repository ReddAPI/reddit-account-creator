import configparser
import argparse
import asyncio
import random

from creator import create_account

config = configparser.ConfigParser()
config.read("config.ini")

API = config["ReddAPI"]["API_KEY"]
PROXY_PATH = config["DATA"]["PROXY_PATH"]
OUTPUT_PATH = config["DATA"]["OUTPUT_PATH"]

headers = {
    "x-rapidapi-key": API,
    "x-rapidapi-host": "reddapi.p.rapidapi.com",
    "Content-Type": "application/json"
}

def load_proxies():
    with open(PROXY_PATH, "r") as f:
        return f.read().splitlines()
    
def save_account(account:str):
    with open(OUTPUT_PATH, "a") as f:
        f.write(account + "\n")
    
proxies = load_proxies()
    
async def create_account_task(proxy: str, headers: dict):
    print(f"CERATING ACCOUNT WITH PROXY [{proxy[:40]}]")
    r = await create_account(proxy, headers)
    
    if r.get("success"):
        print(f'[{r.get("username")}] ACCOUNT CREATED')
        save_account(f'{r.get("email")}:{r.get("username")}:{r.get("password")}')
    
    else:
        print(f"FAILD TO CREATE ACCOUNT WITH RESPONSE [{r}]")


async def main(iterations: int):
    tasks = []
    for _ in range(iterations):
        proxy = random.choice(proxies)
        tasks.append(create_account_task(proxy, headers))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create Reddit accounts using specified proxies.")
    parser.add_argument("iterations", type=int, help="Number of accounts to create")
    args = parser.parse_args()

    asyncio.run(main(args.iterations))
