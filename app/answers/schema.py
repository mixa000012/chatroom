from enum import Enum
import uuid
from typing import List

import re
from pydantic.main import BaseModel


class AnswerBase(BaseModel):
    option_id: uuid.UUID

    class Config:
        orm_mode = True


class AnswerCreate(AnswerBase):
    pass


class AnswerUpdate(AnswerBase):
    pass
