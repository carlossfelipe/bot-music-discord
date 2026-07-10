import asyncio
import os
from dotenv import load_dotenv

from bot import bot


async def main():
    
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    if not TOKEN:
        print("Token não encontrado!")
        return

    async with bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())