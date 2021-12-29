import asyncio

from pyrogram import idle
from pytgcalls import idle

from config import call_py


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | Dark Prince Started! |
    ------------------
"""
    )
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
