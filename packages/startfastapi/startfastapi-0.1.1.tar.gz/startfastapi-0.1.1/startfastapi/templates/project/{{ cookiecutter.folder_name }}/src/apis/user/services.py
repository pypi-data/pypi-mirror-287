from sqlalchemy.ext.asyncio import AsyncSession
from src.apis.service import BaseService
from src.apis.user.models import UserModel
from src.apis.user.schemas import UserCreateSchema, UserInfoSchema, UserUpdateSchema


class UserService(BaseService[UserModel, UserCreateSchema, UserUpdateSchema, UserInfoSchema]):

    model: UserModel = UserModel

    def __init__(self, db_session: AsyncSession):
        super().__init__(model=self.model, session=db_session)