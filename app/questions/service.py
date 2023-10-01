from fastapi import APIRouter, Request, FastAPI, WebSocket, WebSocketDisconnect
from app.core import store
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.core.deps import get_db
from app.questions.schema import QuestionCreate


async def create_request(obj_in: RequestCreate, db: AsyncSession = Depends(get_db),
                         current_user: User = Depends(get_current_user_from_token)):
    obj_in_dict = obj_in.dict()
    obj_in_dict["owner_id"] = current_user.user_id
    return await store.requests.create(db, obj_in=obj_in_dict)
