import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YinsRobot.events import register
from YinsRobot import telethn as tbot

yinzver = "2.0.22"
PHOTO = "https://telegra.ph/file/c05b3fd99bb2cf3eaa270.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'ᴍ Bᴀʙʏʟᴀ Rᴏʙᴏᴛ.** \n\n"
  TEXT += "㋭ **I'ᴍ ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ** \n\n"
  TEXT += f"㋭ **ᴏᴡɴᴇʀ : [ʙᴀʙʏʟᴀ](https://t.me/xbbyla)** \n\n"
  TEXT += f"㋭ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ    :** `{telever}` \n\n"
  TEXT += f"㋭ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ   :** `{tlhver}` \n\n"
  TEXT += f"㋭ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += f"㋭ **ʙᴀʙʏʟᴀʀᴏʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `{yinzver}` \n\n"
  TEXT += "**Thanks For Adding Me Here ㋭**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Babylamusicbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/senjaasupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
