from aiogram import executor, types

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    allowed_updates = [
        types.update.AllowedUpdates.CHAT_MEMBER,
        types.update.AllowedUpdates.MY_CHAT_MEMBER,
        types.update.AllowedUpdates.MESSAGE,
    ]
    executor.start_polling(dp, on_startup=on_startup, allowed_updates=allowed_updates)
