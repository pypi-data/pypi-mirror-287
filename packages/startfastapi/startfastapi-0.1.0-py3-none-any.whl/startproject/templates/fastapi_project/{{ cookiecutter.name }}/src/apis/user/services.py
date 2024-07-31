from src.apis.service import BaseService
from src.apis.user.models import UserModel
from src.apis.user.schemas import UserCreateSchema, UserInfoSchema, UserUpdateSchema


class UserService(BaseService[UserModel, UserCreateSchema, UserUpdateSchema, UserInfoSchema]):
    pass