import pytest
from uuid import uuid4
from sqlalchemy import insert, select

from app.user.schema import UserCreate
from conftest import async_session_maker
from app.user.model import Roles, PortalRole
from app.core import store
from utils.hashing import Hasher
from conftest import create_test_auth_headers_for_user


async def test_delete_user(client):
    user_data = {
        "nickname": "string",
        "password": "string"
    }
    async with async_session_maker() as session:
        stmt = insert(Roles).values(id=uuid4(), role=PortalRole.ROLE_PORTAL_USER)
        await session.execute(stmt)
        await session.commit()
        role = await store.user.get_role(session, PortalRole.ROLE_PORTAL_USER)
        user = await store.user.create(
            session,
            obj_in=UserCreate(
                nickname=user_data.get('nickname'),
                password=Hasher.get_hashed_password(user_data.get('password')),
                admin_role=role
            ))

    resp = await client.delete(
        f"/user/?user_id={user_data.get('user_id')}",
        headers=create_test_auth_headers_for_user(user_data.get('user_id')),
    )
    assert resp.status_code == 200
    # assert resp.json() == {"deleted_user_id": str(user_data["user_id"])}
    # users_from_db = await get_user_from_database(user_data["user_id"])
    # user_from_db = dict(users_from_db[0])
    # assert user_from_db["name"] == user_data["name"]
    # assert user_from_db["surname"] == user_data["surname"]
    # assert user_from_db["email"] == user_data["email"]
    # assert user_from_db["is_active"] is False
    # assert user_from_db["user_id"] == user_data["user_id"]
