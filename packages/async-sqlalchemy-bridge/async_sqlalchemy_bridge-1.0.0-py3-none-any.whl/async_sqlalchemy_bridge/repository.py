from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Any, Union, Type
from uuid import UUID

from sqlalchemy import Select, select, Delete, delete, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

T = TypeVar("T")
K = TypeVar("K", bound=DeclarativeMeta)
ID = TypeVar("ID", int, str, UUID)


class Repository(ABC):
    @abstractmethod
    async def create(self, entity: T) -> T:
        """Создает новый объект"""
        pass

    @abstractmethod
    async def update(self, entity: T) -> T:
        """Обновляет существующий объект"""
        pass

    @abstractmethod
    async def upsert(self, entity: T, **kwargs) -> T:
        """Вставляет или обновляет объект"""
        pass

    @abstractmethod
    async def delete_all(self, entities: list[T]) -> None:
        """Удаляет объект"""
        pass

    @abstractmethod
    async def find_by(self, **kwargs) -> Optional[T]:
        """Найти объект по критериям"""
        pass

    @abstractmethod
    async def find_all_by(self, **kwargs) -> List[T]:
        """Найти все объекты по критериям"""
        pass

    @abstractmethod
    async def find_all(self) -> List[T]:
        """Найти все объекты"""
        pass


class CrudRepository(Repository):
    _table: K = None

    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def create(self, entity: K) -> K:
        self._session.add(entity)
        await self._session.flush()
        return entity

    async def update(self, entity: K) -> K:
        self._session.add(entity)
        return entity

    async def upsert(self, entity: K, **kwargs) -> K:
        for key, value in kwargs.items():
            if not hasattr(self._table, key):
                raise AttributeError(f"{key} unexpected for {self._table.__class__}")
            setattr(entity, key, value)
        if entity.id is None:
            return await self.create(entity)
        return await self.update(entity)

    async def delete_all(self, entities: list[Union[K, ID]]) -> None:
        """force delete"""
        if not entities:
            raise TypeError("Empty entities")
        first_type: Type = type(entities[0])
        if not all(isinstance(e, first_type) for e in entities):
            raise TypeError("Different entities types")
        if isinstance(first_type, K.__bound__):
            entities = [entity.id for entity in entities]
        elif first_type not in ID.__constraints__:
            raise TypeError("Incorrect types")
        smtp: Delete = delete(self._table).where(self._table.id.in_(entities))
        await self._session.execute(smtp)

    async def find_all_by(
        self,
        *,
        relationships: Optional[dict[str, dict[str, Any]]] = None,
        filters: Optional[dict[str, Any]] = None,
        **another_filters,
    ) -> list[K]:
        """
        :param relationships: Example relationships={"user": {"login": "admin"}}
        :param filters: Example filters={"id": 10}
        :param another_filters: id=10
        filters и another_filters могут быть как вместе, так и по отдельности
        :return:
        """
        smtp: Select = select(self._table)
        if filters:
            smtp = smtp.filter_by(**filters)
        if another_filters:
            smtp = smtp.filter_by(**another_filters)
        if relationships:
            for relation, rel_filters in relationships.items():
                smtp = smtp.join(getattr(self._table, relation)).filter_by(**rel_filters)
        result: Result = await self._session.execute(smtp)
        return result.scalars().unique().all()  # noqa

    async def find_by(
        self,
        *,
        relationships: Optional[dict[str, dict[str, Any]]] = None,
        filters: Optional[dict[str, Any]] = None,
        **another_filters,
    ) -> K:
        """
        :param relationships: Example relationships={"user": {"login": "admin"}}
        :param filters: Example filters={"id": 10}
        :param another_filters: id=10
        filters и another_filters могут быть как вместе, так и по отдельности
        :return:
        """
        smtp: Select = select(self._table)
        if filters:
            smtp = smtp.filter_by(**filters)
        if another_filters:
            smtp = smtp.filter_by(**another_filters)
        if relationships:
            for relation, rel_filters in relationships.items():
                smtp = smtp.join(getattr(self._table, relation)).filter_by(**rel_filters)
        smtp = smtp.limit(1)
        result: Result = await self._session.execute(smtp)
        return result.scalars().unique().first()  # noqa

    async def find_all(self) -> list[K]:
        smtp: Select = select(self._table)
        result: Result = await self._session.execute(smtp)
        return result.scalars().unique().all()  # noqa
