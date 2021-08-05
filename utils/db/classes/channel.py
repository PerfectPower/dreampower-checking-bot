from dataclasses import dataclass

from typing import List

from loader import db


@dataclass
class Channel:
    id: int
    channel_id: int
    url: str
    _ids: str
    lefts: int
    is_monitoring: bool
    notify: int

    def __post_init__(self):
        self.channel_id = int(self.channel_id)
        self.notify = int(self.notify) if self.notify else None
        self.is_monitoring = self.is_monitoring == 1

    @property
    def ids(self):
        return [int(id) for id in self._ids.split(',') if id] if self._ids else []

    def add_user(self, user_id: int):
        if self._ids:
            self._ids += f"{user_id},"
        else:
            self._ids = f"{user_id},"

        self._update('ids', f'"{self.ids}"')

    def set_is_monitoring(self, value: bool):
        self.is_monitoring = value
        self._update('is_monitoring', 1 if value else 0)

    def _update(self, parameter, value):
        sql = f"UPDATE Channels SET `{parameter}` = {value} WHERE id = {self.id}"
        db.execute(sql, commit=True)
