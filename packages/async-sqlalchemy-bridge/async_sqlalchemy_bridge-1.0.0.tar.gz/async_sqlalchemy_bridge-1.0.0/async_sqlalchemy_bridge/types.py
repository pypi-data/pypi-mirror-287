from typing import Protocol, Callable


class Logger(Protocol):
    info: Callable
