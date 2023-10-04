from aiogram.utils.keyboard import InlineKeyboardBuilder


def generate_keyboard(city):
    builder = InlineKeyboardBuilder()
    builder.button(text="Узнать погоду подробнее", callback_data=city)

    return builder.as_markup()
