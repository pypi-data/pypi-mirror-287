from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_session import get_session
from core.factory.database_initiator import BaseOperations
from api.governance.database.db_models.tag_model import TagModel


class TagRepository(BaseOperations[TagModel]):
    """
    Repository class for handling database operations related to Tag models.

    Inherits from BaseOperations[TagModel], providing generic CRUD operations.

    This class inherits all methods from BaseOperations[TagModel].
    """

    def __init__(self, db_session: AsyncSession = Depends(get_session)):
        """
        Initialize the TagRepository.

        Args:
            db_session (Session): The database session to use for operations.
        """
        super().__init__(TagModel, db_session)