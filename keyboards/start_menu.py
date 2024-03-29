from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    button_quiz = InlineKeyboardButton(
        "Начать викторину",
        callback_data="quiz_start"
    )
    button_manga_news = InlineKeyboardButton(
        "Сейчас читают: ",
        callback_data="button_manga_news"
    )

    markup.add(button_manga_news)
    markup.add(button_quiz)
    return markup
