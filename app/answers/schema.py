from enum import Enum
import uuid
from typing import List

import re
from pydantic.main import BaseModel


class AnswerBase(BaseModel):
    option_id: uuid.UUID | None
    question_id: uuid.UUID | None
    is_checked: bool | None
    text: str | None

    class Config:
        orm_mode = True


class AnswerCreate(AnswerBase):
    pass


class AnswerCreateWithId(AnswerCreate):
    user_id: uuid.UUID


class AnswerUpdate(AnswerBase):
    pass


class AnswerShow(AnswerBase):
    id: uuid.UUID
