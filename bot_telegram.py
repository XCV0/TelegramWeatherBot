import asyncio
from aiogram import Bot, Dispatcher
from handlers import client
from weather import get_weather


async def main():
    bot = Bot(token="6394410766:AAF-3G3yKw-9uNk5QoEfr1cniBa19xfYj4Q")
    dp = Dispatcher()

    dp.include_router(client.router)

    get_weather.on_startup()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
