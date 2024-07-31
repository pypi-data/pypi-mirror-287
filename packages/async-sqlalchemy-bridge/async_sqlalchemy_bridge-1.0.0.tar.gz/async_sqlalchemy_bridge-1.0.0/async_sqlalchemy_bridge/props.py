from abc import abstractmethod, ABC
from typing import Type

from pydantic import BaseModel
from sqlalchemy import NullPool

from async_sqlalchemy_bridge import CConnection


class ServerSettings(BaseModel):
    application_name: str


class ConnectArgs(BaseModel):
    statement_cache_size: int = 0
    prepared_statement_cache_size: int = 0
    connection_class: Type[CConnection] = CConnection
    server_settings: ServerSettings


class AbstractEngineProps(BaseModel, ABC):
    url: str
    connect_args: ConnectArgs

    @classmethod
    @abstractmethod
    def initialize(cls, url: str, application_name: str, *args, **kwargs):
        pass


class TestEngineProps(AbstractEngineProps):
    poolclass: Type[NullPool] = NullPool

    @classmethod
    def initialize(cls, url: str, application_name: str = "test", *args, **kwargs) -> "TestEngineProps":
        return cls(
            url=url,
            connect_args=ConnectArgs(
                connection_class=CConnection, server_settings=ServerSettings(application_name=application_name)
            ),
        )


class EngineProps(AbstractEngineProps):
    pool_size: int = 5
    pool_recycle: int = 10
    pool_timeout: int = 20
    max_overflow: int = 0
    query_cache_size: int = 0
    echo: bool = False
    pool_pre_ping: bool = True

    @classmethod
    def initialize(
        cls,
        url: str,
        application_name: str,
        pool_size: int = 5,
        pool_recycle: int = 10,
        pool_timeout: int = 20,
        max_overflow: int = 0,
        query_cache_size: int = 0,
        echo: bool = False,
        pool_pre_ping: bool = True,
        statement_cache_size: int = 0,
        prepared_statement_cache_size: int = 0,
        *args,
        **kwargs
    ) -> "EngineProps":
        return cls(
            url=url,
            pool_size=pool_size,
            pool_recycle=pool_recycle,
            pool_timeout=pool_timeout,
            max_overflow=max_overflow,
            query_cache_size=query_cache_size,
            echo=echo,
            pool_pre_ping=pool_pre_ping,
            connect_args=ConnectArgs(
                statement_cache_size=statement_cache_size,
                prepared_statement_cache_size=prepared_statement_cache_size,
                connection_class=CConnection,
                server_settings=ServerSettings(application_name=application_name),
            ),
        )
