import os
import time
import asyncio
import uvloop

# Pyrogram imports
from pyrogram import types
from pyrogram import Client
from pyrogram.errors import FloodWait

# aiohttp imports
from aiohttp import web
from typing import Union, Optional, AsyncGenerator

# telethon imports 
from telethon import TelegramClient
from telethon.sessions import StringSession

# local imports
from web import web_app
from info import LOG_CHANNEL, API_ID, API_HASH, BOT_TOKEN, USER_STRING_SESSION, PORT, BIN_CHANNEL, ADMINS, DATABASE_URL, TAMILMV_LOG, TAMILBLAST_LOG
from utils import temp, get_readable_time
from plugins.scrapper.tools.rss_feed import tamilmv_rss_feed, tamilblasters_rss_feed, tamilrockers_rss_feed

# pymongo and database imports
from database.users_chats_db import db
from database.ia_filterdb import Media
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Bot(Client):
    def __init__(self):
        super().__init__(
            name='Auto-Filter-Bot',
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        client = MongoClient(DATABASE_URL, server_api=ServerApi('1'))
        
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("Something Went Wrong While Connecting To Database!", e)
            exit()

        await super().start()

        if os.path.exists('restart.txt'):
            with open("restart.txt") as file:
                chat_id, msg_id = map(int, file)
            try:
                await self.edit_message_text(chat_id=chat_id, message_id=msg_id, text='Restarted Successfully!')
            except:
                pass
            os.remove('restart.txt')
        
        temp.BOT = self
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        username = '@' + me.username
        print(f"{me.first_name} is started now 🤗")
        
        app = web.AppRunner(web_app)
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()
        
        try:
            await self.send_message(chat_id=LOG_CHANNEL, text=f"<b>{me.mention} Restarted! 🤖</b>")
        except:
            print("Error - Make sure bot admin in LOG_CHANNEL, exiting now")
            exit()
        
        try:
            m = await self.send_message(chat_id=BIN_CHANNEL, text="Test")
            await m.delete()
        except:
            print("Error - Make sure bot admin in BIN_CHANNEL, exiting now")
            exit()
        
        for admin in ADMINS:
            await self.send_message(chat_id=admin, text="<b>✅ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ</b>")
        for chat in [TAMILMV_LOG, TAMILBLAST_LOG]:
            await self.send_message(chat, "Bot Started!")
        
        while True:
            print("TamilMV Scraper Running...")
            await tamilmv_rss_feed(self)
            
            print("TamilBlasters Scraper Running...")
            await tamilblasters_rss_feed(self)        

async def main():
    user_client = TelegramClient(StringSession(USER_STRING_SESSION), API_ID, API_HASH)
    await user_client.start()

    bot = Bot()
    try:
        await bot.start()
        print("Bot Started Successfully")
    except FloodWait as vp:
        wait_time = get_readable_time(vp.value)
        print(f"Flood Wait Occurred, Sleeping For {wait_time}")
        await asyncio.sleep(vp.value)
        print("Now Ready For Deploying!")
        await bot.start()
    
    await bot.idle()  # This keeps the bot running until it's stopped

if __name__ == "__main__":
    asyncio.run(main())  # Replacing the deprecated loop with asyncio.run()
