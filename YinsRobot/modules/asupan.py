# 🥂 © @inisenja

# ⚠️ Don't Remove Credits

import os

import random

from telethon.tl.types import InputMessagesFilterPhotos

from telethon.tl.types import InputMessagesFilterVideo

from YinsRobot.events import register

from YinsRobot import telethn as tbot, ubot2                 

@register(pattern="^/asupan ?(.*)")

async def _(event):

    memeks = await event.reply("**Mencari Video Asupan...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@Database_TonicUbot", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Asupan nya Kak 🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Asupannya gaada komsol")


@register(pattern="^/ayang ?(.*)")

async def _(event):

    try:
        ayangnya = [

            ayang

            async for ayang in event.client.iter_messages(

                "@CeweLogoPack", filter=InputMessagesFilterPhotos

            )

        ]
        aing = await event.client.get_me()

        await event.client.send_file(

            event.chat_id,

            file=random.choice(ayangnya),

            caption=f"**Ayang nya** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()

    except Exception:

        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA CAKEP!.**")


@register(pattern="^/ncp ?(.*)")

async def _(event):

    try:

        kontenrexnya = [

            kontenrex

            async for kontenrex in event.client.iter_messages(

                "@durovbgst", filter=InputMessagesFilterPhotos

            )

        ]
        xa = await event.client.get_me()

        await event.client.send_file(

            event.chat_id,

            file=random.choice(kontenrexnya),

            caption=f"adult photos by [{owner}](tg://user?id={xa.id})",
        )
        await event.delete()

    except Exception:

        await event.edit("**tidak ditemukan. **")
