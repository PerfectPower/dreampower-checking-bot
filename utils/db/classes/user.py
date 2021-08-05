from dataclasses import dataclass
from datetime import datetime

from loader import db

@dataclass
class User:
    id: int
    _name: str
    premium: bool
    left: int
    boobs: float
    pussy: float
    nipples: float
    color: int
    artifacts: bool
    enhance: bool
    ref: int
    _banned: bool
    photos: int
    refs: int
    _date: datetime
    paid: int
    votes: list
    full: bool
    review: bool
    lang: str

    def __post_init__(self):
        self.premium = self.premium == 1
        self.full = self.full == 1
        self.review = self.review == 1
        self.artifacts = self.artifacts == 1
        self.enhance = self.enhance == 1
        self._banned = self._banned == 1
        self.votes = list(map(lambda vote: vote == 't', self.votes))

    async def set_review(self):
        self.review = True
        await self._update('review', 1)

    async def add_left(self, amount: int):
        self.left += amount
        await self._update('lefts', self.left)

    async def _update(self, parameter, value):
        sql = f"UPDATE Users SET `{parameter}` = {value} WHERE `id` = {self.id}"
        db.execute(sql, commit=True)
