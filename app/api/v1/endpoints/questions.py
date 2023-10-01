from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db
from app.user.auth import get_current_user_from_token
from app.core import store

from app.questions.schema import QuestionCreate, QuestionBase

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.post('/')
async def create_question(obj: QuestionCreate, db: AsyncSession = Depends(get_db)) -> QuestionBase:
    question = await store.question.create_question(db=db, obj_in=obj)
    return question


@router.get('/multi')
async def get_question(db: AsyncSession = Depends(get_db)) -> list[QuestionBase]:
    question = await store.question.get_question_with_options(db=db, skip=0, limit=100)
    return question


# todo переписать на service
@router.get('/')
def get_chat(request: Request):
    return templates.TemplateResponse("base.html", {'request': request})
