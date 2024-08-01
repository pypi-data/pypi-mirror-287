from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import db_session
from src.apis.user.services import UserService
from src.apis.user.schemas import UserCreateSchema, UserInfoSchema

router = APIRouter(prefix="/users")


@router.post("")
async def create_user(
    data: UserCreateSchema,
    db_session: AsyncSession = Depends(db_session)
):
    service = UserService(db_session=db_session)
    result: UserInfoSchema = await service.create(data=data)
    return result.model_dump()