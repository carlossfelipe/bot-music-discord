import asyncio
import os
from dotenv import load_dotenv

from bot import bot
from keep_alive import keep_alive


async def main():

    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    if not TOKEN:
        print("Token não encontrado!")
        return
    
    keep_alive()

    async with bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())