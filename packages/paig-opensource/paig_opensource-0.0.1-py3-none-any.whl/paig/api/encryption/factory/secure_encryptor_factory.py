from fastapi import Depends

from api.encryption.database.db_models.encryption_master_key_model import EncryptionMasterKeyModel
from api.encryption.database.db_operations.encryption_master_key_repository import EncryptionMasterKeyRepository
from api.encryption.utils.secure_encryptor import SecureEncryptor


class SecureEncryptorFactory:

    # noinspection PyMethodMayBeStatic
    async def get_secure_encryptor(self, encryption_master_key_repository: EncryptionMasterKeyRepository = Depends(EncryptionMasterKeyRepository)) -> SecureEncryptor:
        """
        Get a secure encryptor

        Args: encryption_master_key_repository (EncryptionMasterKeyRepository): The repository handling encryption
        master key database operations.

        Returns:
            SecureEncryptor: The secure encryptor instance.
        """
        master_key: EncryptionMasterKeyModel = await encryption_master_key_repository.get_active_encryption_master_key()
        return SecureEncryptor(master_key.key)
