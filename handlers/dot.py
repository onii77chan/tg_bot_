from aiogram import types, Dispatcher
from DB.bot_DB import Database
from config import bot
from scrapers.scraper import Scraper


async def button_manga_news(call: types.CallbackQuery):
    db = Database()
    scrap = Scraper()
    data = scrap.scrape_data()
    for title in data:
        db.add_manga_news(
            titles=title)
        if title != '':
            await bot.send_message(
                chat_id=call.from_user.id,
                text=title
            )
        else:
            pass


def register_manga_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        button_manga_news,
        lambda call: call.data == "button_manga_news"
    )
