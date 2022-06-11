# 🥂 © @inisenja

# ⚠️ Don't Remove Credits

import os

import random

from telethon.tl.types import InputMessagesFilterPhotos

from telethon.tl.types import InputMessagesFilterVideo

from YinsRobot.events import register

from YinsRobot import telethn as tbot, ubot2                 

@register(pattern="^/bokep ?(.*)")

async def _(event):

    memeks = await event.reply("**Mencari Video Bokep...🔍**") 

    try:

        bokepnya = [

            bokep

            async for bokep in ubot2.iter_messages(

            "@durovbgst", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(bokepnya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Jangan lupa coli kak 🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Bokepnya gaada komsol")
