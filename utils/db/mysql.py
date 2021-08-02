import logging
from datetime import datetime, timedelta

import pymysql

from data.config import DB


class Database:
    @property
    def connection(self):
        return pymysql.connect(host=DB.host,
                               user=DB.user,
                               password=DB.password,
                               database=DB.name,
                               connect_timeout=10)

    def execute(self, sql: str, parameters: tuple = tuple(), fetchone=False,
                fetchall=False, commit=False):

        connection = self.connection
        cursor = connection.cursor()

        cursor.execute(sql, parameters)

        data = None
        if commit:
            connection.commit()
            data = cursor.lastrowid
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()

        connection.close()

        return data

    def does_table_exist(self, table: str):
        sql = f"SHOW TABLES LIKE '{table}'"
        return self.execute(sql, fetchone=True)

    def drop_table(self, table: str):
        sql = f'DROP TABLE {table}'
        return self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql: str, parameters: dict):
        sql += ' AND '.join([
            f"`{item}` = %s" for item in parameters
        ])
        return sql, tuple(parameters.values())

    @staticmethod
    def log(statement):
        logging.debug(statement)

    # Users

    def get_user(self, id: int):
        sql = f"SELECT * FROM Users WHERE `id` = {id}"
        data = self.execute(sql, fetchone=True)
        if data:
            from utils.db.classes import User
            return User(*data[1:])
        else:
            return None

    # Channels

    def get_channel(self, id: int):
        sql = f'SELECT * FROM Channels WHERE `id` = {id}'
        data = self.execute(sql, fetchone=True)
        if data:
            from utils.db.classes import Channel
            return Channel(*data)
        else:
            return None

    def get_channels(self, sort_by_lefts=True):
        sql = f'SELECT * FROM Channels'
        if sort_by_lefts:
            sql += ' ORDER BY `lefts` DESC'
        from utils.db.classes import Channel
        goods = []
        for data in self.execute(sql, fetchall=True):
            good = Channel(*data)
            goods.append(good)
        return goods