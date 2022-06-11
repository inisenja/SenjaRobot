# 🥂 © @inisenja

# ⚠️ Don't Remove Credits

import os

import random

from telethon.tl.types import InputMessagesFilterPhotos

from telethon.tl.types import InputMessagesFilterVideo

from YinsRobot.events import register

from YinsRobot import telethn as tbot, ubot2                 

@register(pattern="^/ayang ?(.*)")

async def _(event):

    memeks = await event.reply("**Mencari Foto Ayang...🔍**") 

    try:

        ayangnya = [

            ayang

            async for ayang in ubot2.iter_messages(

            "@Database_TonicUbot", filter=InputMessagesFilterPhotos

            )

        ]

        kontols = random.choice(ayangnya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Ayang nya Kak 🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Ayangnya gaada komsol")
