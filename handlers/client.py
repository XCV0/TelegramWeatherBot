from aiogram import types
from aiogram.filters import CommandStart
from create_bot import dp, bot


@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!\n"
                                                 "Этот бот поможет тебе узнать погоду в любом городе\n"
                                                 "Напиши название города")


@dp.message()
async def get_city_input(message: types.Message):
    pass
