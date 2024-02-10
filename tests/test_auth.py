from sqlalchemy import insert, select

from src.auth.models import Role
from conftest import client, async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(Role).values(id=1, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(Role)
        result = await session.execute(query)
        assert result.all() == [(1, 'admin', None)], "This role was not added to DB"


def test_register():
    response = client.post("auth/register", json={
        "email": "username@mamail.com",
        "password": "His_PaSsWoRd",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "Username",
        "role_id": 1
    })

    assert response.status_code == 201, f"Status code is not 201. It is {response.status_code}"
