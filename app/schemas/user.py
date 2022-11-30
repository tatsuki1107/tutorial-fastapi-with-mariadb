from typing import List
from pydantic import BaseModel
from uuid import UUID
from .book import Book


class User(BaseModel):
    uuid: UUID
    username: str

    class Config:
        orm_mode = True


class UserDetail(User):
    books: List[Book] = []
