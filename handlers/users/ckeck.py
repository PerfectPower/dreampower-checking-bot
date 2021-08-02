from aiogram import types

from filters import IsAdmin
from loader import dp


@dp.message_handler(IsAdmin(), commands='check')
async def bot_check(message: types.Message):
    await message.answer('Работаю...')