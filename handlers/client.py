from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from weather import get_weather

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет!\n"
        "Этот бот вам поможет узнать погоду в любом городе\n"
        "Напишите название города"
    )


@router.message()
async def answer_yes(message: Message):
    await message.answer(
        # get_weather.get_weather(city=message.text)
    )
