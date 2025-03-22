import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from database import db  

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@Client.on_message(filters.command("users") & filters.private)
async def users_handler(client: Client, message: Message):
    user_count = len(await db.fetch_all("users"))
    await message.reply(f"👥 **Total Users:** {user_count}")
