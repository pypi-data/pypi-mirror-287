from typing import (
    Optional,
    List,
    TypeVar,
    Generic
)
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import db_session
from src.apis.model import ModelType


CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel, covariant=True)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel, covariant=True)
InfoSchemaType = TypeVar("InfoSchemaType", bound=BaseModel, covariant=True)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType, InfoSchemaType]):
    """
    Base Service
    """
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def create(self, data: CreateSchemaType) -> InfoSchemaType:
        """
        Create API
        """

        # 创建时，不需要设置 exclude_unset=True。
        record = ModelType(**data.model_dump())
        self.session.add(record)
        await self.session.commit()
        await self.session.refresh(record)
        return record

    async def delete(self, id: str) -> int:
        """
        Delete API
        """

        record = await self.session.execute(delete(ModelType).where(ModelType.id == id))
        await self.session.commit()
        return record.rowcount

    async def delete_all(self) -> int:
        """
        Delete All API
        """

        record = await self.session.execute(delete(ModelType))
        await self.session.commit()
        return record.rowcount

    async def update(self, id: str, *, data: UpdateSchemaType) -> int:
        """
        Update API
        """

        record = await self.session.execute(
            update(ModelType).where(ModelType.id == id).values(**data.model_dump(exclude_unset=True))  # 更新时，只更新设置的内容。
        )
        await self.session.commit()
        return record.rowcount

    async def info(self, id: str) -> Optional[InfoSchemaType]:
        """
        Info API
        """

        record = await self.session.execute(select(ModelType).where(ModelType.id == id))
        return record.scalars().first()

    async def list(self, offset: int, limit: int, desc: int) -> List[InfoSchemaType]:
        """
        List API
        """

        record = select(ModelType).offset(offset).limit(limit)

        if desc == 1:
            record = record.order_by(ModelType.updated_at.desc())
        else:
            record = record.order_by(ModelType.updated_at)
        record = await self.session.execute(record)

        return record.scalars().all()

    async def total(self) -> int:
        """
        Total API
        """

        record = await self.session.execute(select(func.count(ModelType.id)))
        return record.scalars().first()
