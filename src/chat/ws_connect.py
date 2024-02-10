import aiohttp
import asyncio
import time

from src.config import MAIN_HOST


async def main():
    async with aiohttp.ClientSession() as session:
        client_id = int(time.time())
        async with session.ws_connect(f"{MAIN_HOST}/chat/ws/{client_id}") as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_chat.log", "a") as log:
                        log.write(f"{msg.data}\n")


asyncio.run(main())
