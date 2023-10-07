from app.questions.model import QuestionTypeEnum
import uuid
from typing import List

import re
from pydantic.main import BaseModel


class OptionSchema(BaseModel):
    text: str



class OptionCreate(OptionSchema):
    class Config:
        orm_mode = True


class QuestionBase(BaseModel):
    text: str
    options: List[OptionCreate]
    survey_id: uuid.UUID
    type: QuestionTypeEnum
    class Config:
        orm_mode = True


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass
