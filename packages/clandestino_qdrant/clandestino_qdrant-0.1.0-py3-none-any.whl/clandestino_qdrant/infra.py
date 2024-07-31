import os

from contextlib import asynccontextmanager

from decouple import AutoConfig
from qdrant_client import AsyncQdrantClient

config = AutoConfig(search_path=os.getcwd())


class QdrantInfra:
    __client: AsyncQdrantClient | None = None

    @classmethod
    def __get_client(cls) -> AsyncQdrantClient:
        if cls.__client is None:
            str_connection = config("CLANDESTINO_QDRANT_CONNECTION_STRING")
            api_key = config("CLANDESTINO_QDRANT_CONNECTION_STRING", default=None)
            cls.__client = AsyncQdrantClient(url=str_connection, api_key=api_key, https=False)
        return cls.__client

    @classmethod
    async def __close_client(cls) -> None:
        if cls.__client is not None:
            cls.__client = None

    @classmethod
    @asynccontextmanager
    async def get_client(cls) -> AsyncQdrantClient:
        async_client = None
        try:
            async_client = cls.__get_client()
            yield async_client
        except Exception as e:
            print(f"{cls.__class__}::get_client")
            raise e
        finally:
            if async_client:
                await cls.__close_client()
