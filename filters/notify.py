from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import db


class IsNotifyUser(BoundFilter):
    async def check(self, message: types.Message):
        user_ids = [channel.notify for channel in db.get_channels() if channel.notify]
        return message.chat.id in user_ids
