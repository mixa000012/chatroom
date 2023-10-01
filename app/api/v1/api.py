from fastapi import APIRouter

from app.api.v1.endpoints import user, questions

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(questions.router, prefix="/questions", tags=["questions"])
