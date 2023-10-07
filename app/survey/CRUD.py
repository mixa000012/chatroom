from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.db.CRUD import ModelAccessor, CreateSchemaType, ModelType
from app.survey.model import Survey
from app.questions.model import Question
from app.survey.schema import SurveyBase, SurveyUpdate, SurveyCreate


class SurveyAccessor(ModelAccessor[Survey, SurveyCreate, SurveyUpdate]):
    async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in)  # type: ignore
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_questions(self, id, db: AsyncSession):
        survey = await db.execute(
            select(Survey).options(selectinload(Survey.questions).selectinload(Question.options)).where(Survey.id == id)
        )
        survey = survey.scalar()
        return survey


survey = SurveyAccessor(Survey)
