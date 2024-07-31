import datetime
import hashlib
import uuid

from clandestino_interfaces import IMigrateRepository
from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import MatchValue
from qdrant_client.models import VectorParams, Distance, Filter, FieldCondition

from .infra import QdrantInfra


class QdrantMigrateRepository(IMigrateRepository, QdrantInfra):

    @classmethod
    def get_control_collection(cls):
        return "clandestino"

    @classmethod
    async def create_control_table(cls) -> None:
        control_collection = cls.get_control_collection()
        async with cls.get_client() as client:
            await client.create_collection(
                collection_name=control_collection,
                vectors_config=VectorParams(size=1, distance=Distance.COSINE),
            )

    @classmethod
    async def control_table_exists(cls) -> bool:
        control_collection = cls.get_control_collection()
        async with cls.get_client() as client:
            try:
                await client.get_collection(collection_name=control_collection)
                return True
            except Exception:
                return False

    @staticmethod
    def hash_name(name: str):
        hash_object = hashlib.sha256(name.encode('utf-8'))
        hex_dig = hash_object.hexdigest()[:32]
        return str(uuid.UUID(hex=hex_dig))

    @classmethod
    async def register_migration_execution(cls, migration_name: str) -> None:
        control_collection = cls.get_control_collection()
        async with cls.get_client() as client:
            await client.upsert(
                collection_name=control_collection,
                points=[{
                    "id": cls.hash_name(migration_name),
                    "vector": [1],
                    "payload": {
                        "name": migration_name,
                        "created_at": str(datetime.datetime.utcnow())
                    }
                }]
            )

    @classmethod
    async def remove_migration_execution(cls, migration_name: str) -> None:
        control_collection = cls.get_control_collection()
        async with cls.get_client() as client:
            await client.delete(
                collection_name=control_collection,
                points_selector=[cls.hash_name(migration_name)]
            )

    @classmethod
    async def migration_already_executed(cls, migration_name: str) -> bool:
        control_collection = cls.get_control_collection()
        async with cls.get_client() as client:
            client: AsyncQdrantClient = client
            result = await client.search(
                collection_name=control_collection,
                query_filter=Filter(
                    must=[
                        FieldCondition(
                            key="name",
                            match=MatchValue(
                                value=migration_name,
                            ),
                        )
                    ]
                ),
                query_vector=[1],
                limit=1
            )
            return bool(result)
