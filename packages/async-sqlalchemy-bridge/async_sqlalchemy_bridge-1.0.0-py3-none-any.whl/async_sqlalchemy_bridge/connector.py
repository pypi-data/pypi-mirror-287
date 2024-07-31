from uuid import uuid4

from asyncpg import Connection


class CConnection(Connection):
    """
    Custom connection class that extends the `Connection` class.

    Explanation:
        This class provides a custom implementation of the `_get_unique_id` method, which generates a unique ID
        with the given prefix using the `uuid4` function.
    Methods:
        _get_unique_id: Generates a unique ID with the given prefix.

    Returns:
        str: The generated unique ID.
    """

    def _get_unique_id(self, prefix: str) -> str:
        """
        :param prefix: The prefix to use for the unique ID.
        :return: Id
        """
        return f"__asyncpg_{prefix}_{uuid4()}__"
