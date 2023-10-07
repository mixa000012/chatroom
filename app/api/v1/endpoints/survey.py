import uuid

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db
from app.user.auth import get_current_user_from_token
from app.survey import service
from app.user.model import User
from app.survey.schema import SurveyCreate, SurveyBase, SurveyShow

router = APIRouter()


@router.post('/')
async def create_survey(obj: SurveyCreate, db: AsyncSession = Depends(get_db),
                        current_user: User = Depends(get_current_user_from_token)):
    answer = await service.create_survey(db=db, obj_in=obj, current_user=current_user)
    return answer


@router.get('/')
async def get_questions(id: uuid.UUID, db: AsyncSession = Depends(get_db)) -> SurveyShow:
    answers = await service.get_questions(id=id, db=db)
    return answers