from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import forbidden_messages


class IsForbiddenMessage(BoundFilter):
    async def check(self, message: types.Message):
        for forbidden_message in forbidden_messages:
            if forbidden_message in message.text:
                return True
        return False
