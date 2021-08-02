from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import GROUP


class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.id == int(GROUP)