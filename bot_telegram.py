import asyncio
from create_bot import dp, bot


async def main():
    await dp.start_polling(bot)


async def on_startup():
    print("Bot success start up!")


if __name__ == "__main__":
    asyncio.run(main())
