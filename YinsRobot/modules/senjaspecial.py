# Jangan hapus credit ya tot
# powered by @itsmesenjaaah

import random
from YinsRobot.events import register
from YinsRobot import telethn

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
