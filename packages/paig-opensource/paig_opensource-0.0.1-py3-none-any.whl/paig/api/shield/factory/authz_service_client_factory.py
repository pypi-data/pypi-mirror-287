from fastapi import Depends

from api.authz.authorizer.paig_authorizer import PAIGAuthorizer
from api.authz.services.paig_authorizer_service import PAIGAuthorizerService
from api.shield.client.authz_service_rest_http_client import HttpAuthzClient
from api.shield.client.local_authz_service_client import LocalAuthzClient
from api.shield.utils import config_utils


class AuthzServiceClientFactory:
    """
    A factory class for creating authorization service clients.

    Methods:
        get_authz_service_client(client_type: str):
            Returns an instance of the specified authorization service client.
    """

    def __init__(self, paig_authorizer: PAIGAuthorizer = Depends(PAIGAuthorizerService)):
        """
        Constructs a new AuthzServiceClientFactory.

        Args:
            paig_authorizer (PAIGAuthorizer, optional): An instance of PAIGAuthorizer. Defaults to Depends(PAIGAuthorizerService).
        """
        self.paig_authorizer = paig_authorizer

    def get_authz_service_client(self):
        """
        Returns:
            An instance of the specified authorization service client.

        Raises:
            Exception: If the client_type is not "http" or "local".
        """
        client_type = config_utils.get_property_value('authz_client', 'local')
        match client_type:
            case "http":
                return HttpAuthzClient()
            case "local":
                return LocalAuthzClient(self.paig_authorizer)
            case _:
                raise Exception("Invalid service type")
