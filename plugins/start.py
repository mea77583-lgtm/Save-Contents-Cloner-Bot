import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import db  

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    user_id = message.from_user.id
    user = await client.get_me()

    await message.reply(
        f"**Hi {message.chat.first_name}!**\n"
        f"I am {user.first_name}, I can save messages from any **public** channel.\n"
        "Just send me the message link, and I will send it to you.\n\n"
        "**Created by** @SaveContentsBot."
    )
    if not await db.is_inserted(f"users", user_id):
        await db.insert(f"users", user_id)
    if not await db.is_inserted("users", user_id):
        await db.insert("users", user_id)

@Client.on_message(filters.command("source") & filters.private)
async def source_handler(client: Client, message: Message):
    await message.reply(
        "You can get the source code of this bot here!",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Get Now", url="https://github.com/Harshit-shrivastav/Save-Contents-Cloner-Bot")]]
        ),
  )
