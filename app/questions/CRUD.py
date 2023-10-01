from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.core.db.CRUD import ModelAccessor
from app.questions.model import Question, Option
from app.questions.schema import QuestionCreate, QuestionUpdate, OptionCreate


class QuestionAccessor(ModelAccessor[Question, QuestionCreate, QuestionUpdate]):
    async def filter_by_tags(self, tags, db: AsyncSession):
        tags = [i.value for i in tags]
        stmt = (
            select(News).options(selectinload(News.news_tags))
            .join(News.news_tags)  # Join the News and NewsTags tables
            .where(Tag.name.in_(tags))  # Filter by tag names
        )
        results = await db.execute(stmt)
        return results.scalars().all()

    async def create_question(self, db: AsyncSession, obj_in: QuestionCreate):
        question_ = QuestionCreate(question_text=obj_in.question_text, options=[])
        for option_data in obj_in.options:
            option = Option(text=option_data.text, is_correct=option_data.is_correct)
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
        team = question.scalars().all()

        return team

    async def create_tag(self, db: AsyncSession, name):
        # Create a new tag
        new_tag = Tag(name=name)

        # Add and commit to the database
        db.add(new_tag)
        await db.commit()
        await db.refresh(new_tag)
        return new_tag

    async def get_tag(self, db: AsyncSession, tag_name):
        tag = await db.execute(select(Tag).where(Tag.name == tag_name))
        return tag

    async def get_multi_tags(
            self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ):
        stmt = select(Tag).offset(skip).limit(limit)

        team = await db.execute(stmt)
        team = team.scalars().all()

        return team


question = QuestionAccessor(Question)
