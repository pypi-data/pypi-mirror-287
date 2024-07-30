from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_session import get_session
from core.factory.database_initiator import BaseOperations
from api.governance.database.db_models.metadata_key_model import VectorDBMetaDataKeyModel


class MetadataKeyRepository(BaseOperations[VectorDBMetaDataKeyModel]):
    """
    Repository class for handling database operations related to VectorDB Metadata Key models.

    Inherits from BaseOperations[VectorDBMetaDataKeyModel], providing generic CRUD operations.

    This class inherits all methods from BaseOperations[VectorDBMetaDataKeyModel].
    """

    def __init__(self, db_session: AsyncSession = Depends(get_session)):
        """
        Initialize the MetadataRepository.

        Args:
            db_session (Session): The database session to use for operations.
        """
        super().__init__(VectorDBMetaDataKeyModel, db_session)