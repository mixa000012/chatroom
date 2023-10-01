from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.core.db.CRUD import ModelAccessor
from app.questions.model import Question, Option
from app.questions.schema import QuestionCreate, QuestionUpdate, OptionCreate


class QuestionAccessor(ModelAccessor[Question, QuestionCreate, QuestionUpdate]):
    async def create_question(self, db: AsyncSession, obj_in: QuestionCreate):
        question_ = QuestionCreate(question_text=obj_in.question_text, options=[])
        for option_data in obj_in.options:
            option = Option(text=option_data.text)
            question_.options.append(option)
        obj_in_data = question_.dict()
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        await db.commit()
        return db_obj

    async def get_question_with_options(
            self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ):
        stmt = select(Question).options(selectinload(Question.options)).offset(skip).limit(limit)

        question = await db.execute(stmt)
        questions = question.scalars().all()

        return questions


question = QuestionAccessor(Question)
