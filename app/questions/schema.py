from enum import Enum
import uuid
from typing import List

import re
from pydantic.main import BaseModel


class OptionSchema(BaseModel):
    text: str
    is_correct: bool




class OptionCreate(OptionSchema):
    class Config:
        orm_mode = True


class QuestionBase(BaseModel):
    question_text: str
    options: List[OptionCreate]
    class Config:
        orm_mode = True


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass
