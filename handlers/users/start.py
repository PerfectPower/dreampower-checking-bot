from aiogram import types

from filters import IsNotifyUser
from loader import dp, db


@dp.message_handler(IsNotifyUser(), commands='start')
async def bot_check(message: types.Message):
    channels = db.get_channels()

    for channel in channels:
        if channel.notify and channel.notify == message.chat.id:
            text = '\n\n'.join(['Тут бы будете получать уведомления о новый пользователях, которые пришли от бота',
                                'Чтобы выключить уведомления напишите @TimNekk или заблокируйте бота'])
            await message.answer(text)
