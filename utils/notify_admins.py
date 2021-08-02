import logging

from aiogram import Dispatcher

from data.config import ADMIN


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN, "Бот Запущен")

    except Exception as err:
        logging.exception(err)
