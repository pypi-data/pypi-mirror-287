from fastapi import Depends

from api.encryption.services.encryption_key_service import EncryptionKeyService
from api.shield.client.local_account_service_client import LocalAccountServiceClient
from api.shield.client.http_account_service_client import HttpAccountServiceClient
from api.shield.utils import config_utils


class AccountServiceFactory:
    """
    Factory class for creating account service client instances based on configuration.

    Methods:
        get_account_service_client():
            Returns an instance of an account service client based on the configured client type.
    """

    def __init__(self, encryption_key_service: EncryptionKeyService = Depends(EncryptionKeyService)):
        """
        Initializes the AccountServiceClientFactory instance.
        """
        self.encryption_key_service = encryption_key_service

    def get_account_service_client(self):
        """
        Returns an instance of an account service client based on the configured client type.

        Returns:
            object: Instance of an account service client.

        Raises:
            Exception: If an invalid service type is configured in the application.
        """
        client_type = config_utils.get_property_value('account_service_client', 'local')
        match client_type:
            case "http":
                return HttpAccountServiceClient()
            case "local":
                return LocalAccountServiceClient(self.encryption_key_service)
            case _:
                raise Exception(
                    f"Invalid service type: '{client_type}'. Expected 'http' or 'local'. "
                    "Please configure the 'account_service_client' property with a valid service type."
                )
