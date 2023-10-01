from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_db
from app.user.auth import get_current_user_from_token
from app.core import store
from app.user.model import User
from app.answers.schema import AnswerCreate, AnswerBase

router = APIRouter()


@router.post('/')
async def create_answer(obj: AnswerCreate, db: AsyncSession = Depends(get_db),
                        current_user: User = Depends(get_current_user_from_token)) -> AnswerBase:
    answer = await store.answer.create(db=db, obj_in=obj)
    return answer
