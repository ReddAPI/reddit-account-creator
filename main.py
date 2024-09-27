import configparser
import argparse
import asyncio
import logging
import random

from creator import create_account

logger = logging.getLogger("RedditAccountCreator")
logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s] | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )

httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)

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
    """Load proxies from the specified file."""
    try:
        with open(PROXY_PATH, "r") as f:
            proxies = f.read().splitlines()
            logger.info(f"Loaded {len(proxies)} proxies.")
            return proxies
    except Exception as e:
        logger.error(f"Error loading proxies: {e}")
        return []

def save_account(account: str):
    """Append the account details to the output file."""
    try:
        with open(OUTPUT_PATH, "a") as f:
            f.write(account + "\n")
        logger.info(f"Account saved: {account}")
    except Exception as e:
        logger.error(f"Error saving account: {e}")

proxies = load_proxies()

async def create_account_task(proxy: str, headers: dict):
    """Create a Reddit account using the specified proxy."""
    logger.info(f"Creating account with proxy [{proxy[:40]}]")
    response = await create_account(proxy, headers)
    
    if response.get("success"):
        account_info = f'{response.get("email")}:{response.get("username")}:{response.get("password")}'
        logger.info(f'Account created: [{response.get("username")}]')
        save_account(account_info)
    else:
        logger.error(f"Failed to create account with response [{response}]")

async def main(iterations: int):
    """Main function to create multiple accounts concurrently."""
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
