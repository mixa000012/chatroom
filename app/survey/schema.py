from datetime import datetime
from app.questions.schema import QuestionBase
import uuid
from typing import List

from pydantic.main import BaseModel


class SurveyBase(BaseModel):
    name: str
    expire_at: datetime

    class Config:
        orm_mode = True


class SurveyCreate(SurveyBase):
    pass


class SurveyUpdate(SurveyBase):
    pass


class SurveyShow(SurveyBase):
    created_by: uuid.UUID
    created_at: datetime
    id: uuid.UUID
    questions: List[QuestionBase]
