import pytest

from httpx import AsyncClient
from conftest import async_session_maker

from sqlalchemy import insert, select

from src.auth.models import Role


@pytest.mark.parametrize(
    "role_id, name, permissions",
    [
        (1, "admin", None)
    ]
)
async def test_add_role(role_id, name, permissions):
    async with async_session_maker() as session:
        """Here we create a DB and tables. Add the first default role."""
        new_role = {
            "id": role_id,
            "name": name,
            "permissions": permissions
        }
        stmt = insert(Role).values(**new_role)
        await session.execute(stmt)
        await session.commit()

        query = select(Role.id)
        result = await session.execute(query)
        result = result.all()

        assert result == [(new_role["id"], )], (f"The role wasn't added to the database. "
                                                f"result.all() is  {result}")


async def test_register_default_user(ac: AsyncClient):
    """role_id of this User always will be 1. Check logic in src.auth.manager.py. But role_id=1 must exist."""
    response = await ac.post("/auth/register", json={
        "email": "fake_admin@mail.com",
        "password": "password",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "fake_admin",
        "role_id": 111222333
    })

    assert response.status_code == 201, f"Status code is not 201. It is {response.status_code}"
