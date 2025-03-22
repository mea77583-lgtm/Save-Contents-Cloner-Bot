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
        "Just send me the message link, and I will fetch it for you.\n\n"
        "**Created by** @SaveContentClonerBot."
    )

    if not await db.is_inserted("users", user_id):
        await db.insert("users", user_id)

@Client.on_message(filters.command("bulk") & filters.private)
async def bulk_handler(client: Client, message: Message):
    await message.reply(
        "**Get the full version with premium features!**\n\n"
        "✅ Unlimited Bulk Saving\n"
        "✅ Private Channel & Group Support\n"
        "✅ No Time Gaps\n"
        "✅ Host Your Own Bot\n\n"
        "Visit below link to purchase the source code.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💰 Buy Now", url="https://shop.harshit.wtf")]]
        ),
  )
