from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from weather import get_weather
from msg_buttons.user_keybord import generate_keyboard
from openai import chatgpt_advice

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
    w = get_weather.get_weather(city=message.text)

    if w:
        weather_text = f"Сейчас в городе {message.text} {w.detailed_status}" \
                       f"\nНа улице {w.temperature('celsius')['temp']}°C, " \
                       f"ощущается как {w.temperature('celsius')['feels_like']}°C" \
                       f"\nВлажность {w.humidity}%"
        
        openai_query = chatgpt_advice.get_advice(weather=weather_text)
        await message.answer(
            weather_text + f"\nСовет по одежде(By OpenAI){openai_query}",
            reply_markup=generate_keyboard(message.text)
        )
    else:
        await message.answer("Такого города не сущетсвует, попробуйте другой!")


@router.callback_query()
async def more_info(callback: CallbackQuery):
    await callback.answer(text="Function in Develop", show_alert=True)
