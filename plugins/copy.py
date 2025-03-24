import re
import asyncio
import logging
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def copy_msg(sender_id, msg_link, client, message):
    try:
        chat_id = msg_link.split("/")[-2]
        msg_id = int(msg_link.split("/")[-1].split("?")[0])
    except (IndexError, ValueError):
        return await message.reply("❌ **Invalid Link!**")

    try:
        msg = await client.get_messages(chat_id, msg_id)
        if "t.me/c/" in msg_link:
            return await message.reply("❌ This bot only supports public channel messages.")
    except Exception as e:
        return await message.reply(f"❌ Error: {str(e)}")

    try:
        if "?single" in msg_link:
            await client.copy_media_group(sender_id, msg.chat.id, msg.id)
        else:
            await client.copy_message(sender_id, msg.chat.id, msg.id)
    except FloodWait as fw:
        await message.reply(f"⚠️ Telegram limit reached. Try again in {fw.value} seconds.")
        await asyncio.sleep(fw.value)
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")

@Client.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(client: Client, message: Message):
    link_pattern = re.compile(r"https?://t\.me/\S+", re.DOTALL)
    links = re.findall(link_pattern, message.text)

    if not links:
        return await message.reply("⚠️ Send only a valid **Telegram message link**.")

    for link in links:
        if "t.me/c/" in link:
            return await message.reply(
                "**Only public channel links are supported.**\n\n"
                "Get the full version with **private group support** and more!",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("💰 Buy Now", url="https://shop.harshit.wtf")]]
                ),
            )

        await message.reply_chat_action(enums.ChatAction.TYPING)
        await copy_msg(message.chat.id, link, client, message)
