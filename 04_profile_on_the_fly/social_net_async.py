import random

import aiohttp
import asyncio

backend_endpoint = "http://localhost:8000"


async def get_user_name(user_id: int) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{backend_endpoint}/users/{user_id}") as r:
            r.raise_for_status()
            user = await r.json()
            return user["name"]

async def get_user_friends(user_id: int) -> list[int]:
     async with aiohttp.ClientSession() as session:
        async with session.get(f"{backend_endpoint}/friends/{user_id}") as r:
            r.raise_for_status()
            friends = await r.json()
            return friends


async def serf_social_net():
    user_id = 1
    while True:
        name = await get_user_name(user_id)
        friends  = await get_user_friends(user_id)
        user_id = random.choice(friends)


if __name__ == "__main__":
    try:
        asyncio.run(serf_social_net())
    except KeyboardInterrupt:
        pass
