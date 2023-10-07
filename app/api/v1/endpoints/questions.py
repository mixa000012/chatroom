from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db
from app.questions import service
from app.questions.service import SurveyDoesntExist

from app.core import store

from app.questions.schema import QuestionCreate, QuestionBase

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.post('/')
async def create_question(obj: QuestionCreate, db: AsyncSession = Depends(get_db)) -> QuestionBase:
    try:
        question = await service.create_question(obj=obj, db=db)
    except SurveyDoesntExist:
        raise HTTPException(status_code=422, detail="Survey doesn't exists")
    return question


# todo исправить
@router.get('/multi')
async def get_question(db: AsyncSession = Depends(get_db)) -> list[QuestionBase]:
    question = await store.question.get_question_with_options(db=db, skip=0, limit=100)
    return question

# todo переписать на service
