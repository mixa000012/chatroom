from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.core.db.CRUD import ModelAccessor
from app.answers.model import Answer
from app.answers.schema import AnswerCreate, AnswerUpdate


class AnswerAccessor(ModelAccessor[Answer, AnswerCreate, AnswerUpdate]):
    pass


answer = AnswerAccessor(Answer)
