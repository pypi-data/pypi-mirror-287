from enum import Enum
from typing import Optional
from sqlmodel import Field
from src.apis.model import Base
from src.core.security import get_password_hash


class HashedPassword(str):
    """Takes a plain text password and hashes it.

    use this as a field in your SQLModel

    class User(SQLModel, table=True):
        username: str
        password: HashedPassword

    """

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Accepts a plain text password and returns a hashed password."""
        if not isinstance(v, str):
            raise TypeError("string required")

        hashed_password = get_password_hash(v)
        # you could also return a string here which would mean model.password
        # would be a string, pydantic won't care but you could end up with some
        # confusion since the value's type won't match the type annotation
        # exactly
        return cls(hashed_password)


class UserStatus(Enum):
    SUPER_USER: int = 0
    NORMAL_USER: int = 1 << 1
    DELETED_USER: int = 1 << 2


class UserModel(Base, table=True):
    """
    User Model
    """

    __tablename__ = "user"

    username: str = Field(nullable=False, unique=True, index=True, min_length=1, max_length=32)
    password: HashedPassword = Field(nullable=False, unique=False)
    status: Optional[UserStatus] = Field(default=UserStatus.NORMAL_USER, nullable=True, unique=False)