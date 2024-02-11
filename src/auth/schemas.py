import uuid

from pydantic import EmailStr, BaseModel, Json
from fastapi_users import schemas

from typing import Optional
from datetime import datetime


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: uuid.UUID
    username: str
    email: EmailStr
    registered_at: datetime
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    role_id: int


class RoleCreate(BaseModel):
    id: int
    name: str
    permissions: str
