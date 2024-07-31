import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Optional, Tuple

from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from async_sqlalchemy_bridge import AbstractEngineProps
from async_sqlalchemy_bridge.types import Logger


class AsyncDataBase:
    """
    Represents a database instance with singleton behavior.

    Explanation:
        This class serves as a singleton database instance. It provides methods for obtaining an async session,
        initializing the logging of compiled SQL queries, and accessing the database engine and base class.

    Methods:
        __new__: Overrides the __new__ method to implement a singleton pattern.
        __init__: Initializes the database instance.
        get_async_session: Returns an asynchronous context manager that provides an async session.
        init_echo_compiled_query: Initializes the logging of compiled SQL queries after each cursor execution.
    """

    __instance: Optional["AsyncDataBase"] = None

    __slots__ = ("_engine", "_async_session_maker")

    def __new__(cls, *args, **kwargs):
        """
        Overrides the __new__ method to implement a singleton pattern.
        Returns:
            The instance of the class.
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, props: AbstractEngineProps) -> None:
        """
        async_session_maker: The async session maker.
        engine: The database engine.
        """
        self._engine: AsyncEngine = create_async_engine(**props.model_dump())
        self._async_session_maker = async_sessionmaker(self._engine, class_=AsyncSession, expire_on_commit=False)

    async def get_dep_session(self) -> AsyncSession:
        """
        Provide a single asynchronous session for a FastAPI dependency.
        This method is used to automatically manage session lifecycle within FastAPI routes.
        """
        try:
            async with self._async_session_maker() as session:
                session: AsyncSession
                yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        This method can be used to manually manage the session lifecycle,
        allowing 'async with' usage for more complex transactions or local usage.
        """
        async_session: AsyncSession = self._async_session_maker()
        try:
            yield async_session
        except Exception:
            await async_session.rollback()
            raise
        finally:
            await async_session.close()

    @property
    def async_session_maker(self) -> async_sessionmaker:
        return self._async_session_maker

    @property
    def engine(self) -> AsyncEngine:
        return self._engine

    def init_echo_compiled_query(self, log: Optional[Logger] = None) -> None:
        """
        Initializes the logging of compiled SQL queries after each cursor execution.
        Args:
            self: The instance of the class.
            log (Logger): The logger object to use for logging the queries.
        Returns:
            None
        """
        if log is None:
            log = logging.getLogger(__name__)

        @event.listens_for(self._engine.sync_engine, "after_cursor_execute")
        def after_cursor_execute(conn, cursor, statement: str, parameters: Tuple, context, executemany: bool):
            if context.compiled:
                log.info(f"{statement};\t[Params: {parameters}]")
