from aiogram import types
from aiogram.utils.markdown import hcode

from filters import IsAdmin
from loader import dp, db


@dp.message_handler(IsAdmin(), commands=['list'])
async def bot_list(message: types.Message):
    channels = db.get_channels(sort_by_lefts=False)

    text = []
    for channel in channels:
        text += [
            f'{channel.id}) {"✅" if channel.is_monitoring else "❌"} <b>{channel.url}</b> <i>{channel.channel_id}</i>',
            f'Обработок: <b>{channel.lefts}</b>',
            f'Уведомлять: <b>{hcode(channel.notify) if channel.notify else "Не настроено"}</b>'
        ]

    await message.answer('\n'.join(text), disable_web_page_preview=True)
