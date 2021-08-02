from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import db


class IsEditCommand(BoundFilter):
    async def check(self, message: types.Message):
        return message.is_command() and db.get_channel(id=message.text[5:])
