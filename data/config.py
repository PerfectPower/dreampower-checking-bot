from dataclasses import dataclass

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMIN = env.str("ADMIN")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
GROUP = env.str("GROUP")


@dataclass
class DB:
    host = env.str('db_host')
    user = env.str('db_user')
    password = env.str('db_password')
    name = env.str('db_name')


forbidden_messages = [
    'joinchat',
    '?start',
]