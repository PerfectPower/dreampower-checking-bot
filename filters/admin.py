from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMIN


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return str(message.chat.id) in ADMIN
