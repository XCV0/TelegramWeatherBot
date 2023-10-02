import asyncio
from aiogram import Bot, Dispatcher
from handlers import client
from weather import get_weather


async def main():
    bot = Bot(token="TOKEN")
    dp = Dispatcher()

    dp.include_router(client.router)

    await get_weather.on_startup()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())