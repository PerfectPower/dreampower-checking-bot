import logging

from aiogram import types
from aiogram.utils.markdown import hcode

from data.config import ADMIN
from loader import dp, db


@dp.chat_member_handler()
async def test(message: types.Message):
    channels = db.get_channels()

    for channel in channels:
        if channel.channel_id == message.chat.id:

            status = message['new_chat_member']['status']
            if status == 'member':

                user_id = message.from_user.id
                user = db.get_user(id=user_id)
                if user and user_id not in channel.ids:
                    await user.add_left(channel.lefts)
                    channel.add_user(user.id)
                    logging.info(f'Пользователю {user.id} выдано {channel.lefts} обработок за подписку на {channel.url}')

                    if channel.notify:
                        try:
                            await dp.bot.send_message(channel.notify, f'Пользователь <b>{user._name}</b> ({hcode(user.id)}) подписался на канал')
                        except:
                            pass

            return

    print(message['new_chat_member']['status'])


@dp.my_chat_member_handler()
async def bot_join_channel(message: types.Message):
    channels = db.get_channels()

    for channel in channels:
        if channel.channel_id == message.chat.id:
            status = message['new_chat_member']['status']

            if status == 'left':
                channel.set_is_monitoring(False)
                text = f"Бот больше не чекает канал {channel.url}"
            else:
                channel.set_is_monitoring(True)
                text = f"Бот начал чекать канал {channel.url}"

            logging.info(text)
            await dp.bot.send_message(ADMIN, text)
            if channel.notify:
                try:
                    await dp.bot.send_message(channel.notify, text)
                except:
                    pass

            return
