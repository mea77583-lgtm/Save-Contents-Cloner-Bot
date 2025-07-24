import asyncio
import re
from pyrogram import Client, idle
from database import db
from config import Telegram

# ------------------------------------------------------------------
class _Registry:
    _tokens = set()

    @staticmethod
    def is_running(token: str) -> bool:
        return token in _Registry._tokens

    @staticmethod
    def add(token: str):
        _Registry._tokens.add(token)

    @staticmethod
    def remove(token: str):
        _Registry._tokens.discard(token)
# ------------------------------------------------------------------

async def start_client(token: str):
    if _Registry.is_running(token):
        return

    client_name = re.sub(r'[^a-zA-Z0-9]', '', token)
    client = Client(
        in_memory=True,
        name=client_name,
        api_id=Telegram.API_ID,
        api_hash=Telegram.API_HASH,
        bot_token=token,
        plugins={"root": "plugins"}
    )

    try:
        await client.start()
        _Registry.add(token)
        await idle()          
    except Exception:
        pass                  
    finally:
        _Registry.remove(token)
        await client.stop()

async def main():
    bot_tokens = await db.fetch_all("tokens")
    tasks = [
        start_client(token)
        for token in bot_tokens
        if not _Registry.is_running(token)
    ]
    await asyncio.gather(*tasks)
    print('All clients booted (or already running)')

if __name__ == "__main__":
    asyncio.run(main())
