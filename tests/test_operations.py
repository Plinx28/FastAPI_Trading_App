from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/operations/", json={
        "operation_number": "123432",
        "quantity": "string",
        "figi": "string",
        "instrument_type": "string",
        "date": "2024-01-27T19:22:01",
        "type": "Выплата купонов"
    })

    assert response.status_code == 200


async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/operations/", params={
        "operation_type": "Выплата купонов",
    })

    assert response.status_code == 200
    # assert response.json()["status"] == "success"
    # assert len(response.json()["data"]) == 1 
