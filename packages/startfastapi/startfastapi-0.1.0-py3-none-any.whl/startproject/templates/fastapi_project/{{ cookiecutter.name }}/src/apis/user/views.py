from fastapi import APIRouter
from src.apis.user.services import UserService
from src.apis.user.schemas import UserCreateSchema, UserInfoSchema

router = APIRouter(prefix="/users")


@router.post("")
async def create_user(
    data: UserCreateSchema,
):
    service = UserService()
    result: UserInfoSchema = await service.create(data=data)
    return result.model_dump()