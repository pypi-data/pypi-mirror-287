from clandestino_interfaces import AbstractMigration
from clandestino_qdrant.infra import QdrantInfra


class Migration(AbstractMigration):

    infra = QdrantInfra()

    async def up(self) -> None:
        """Do modifications in database"""
        pass

    async def down(self) -> None:
        """Undo modifications in database"""
        pass
