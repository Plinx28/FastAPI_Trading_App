from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from fastapi_cache.decorator import cache

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.operations.models import Operation
from src.operations.schemas import OperationCreate
from src.database import get_async_session

import time

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/long_operation")
@cache(expire=60)
def get_long_on():
    time.sleep(4)
    return "A lot of data which calculated for a hundred years."


@router.get("/")
async def get_specific_operations(
        operation_type: str,
        session: AsyncSession = Depends(get_async_session)
        ):
    try:
        query = select(Operation).where(Operation.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": "You've got all specific operations from your quory."
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
