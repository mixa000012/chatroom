from enum import Enum
import uuid
from pydantic import EmailStr
import re
from pydantic.main import BaseModel


class PortalRole(str, Enum):
    ROLE_PORTAL_USER = "ROLE_PORTAL_USER"
    ROLE_PORTAL_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_PORTAL_SUPERADMIN = "ROLE_PORTAL_SUPERADMIN"


class UserBase(BaseModel):
    nickname: str
    password: str


class UserCreate(UserBase):
    roles: list[PortalRole]


class UserUpdateData(UserBase):
    pass


class User_(UserUpdateData):
    user_id: uuid.UUID

    class Config:
        orm_mode = True


class UserShow(BaseModel):
    user_id: uuid.UUID
    email: EmailStr

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    access_token: str
    token_type: str
