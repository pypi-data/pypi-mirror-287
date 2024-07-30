from fastapi import APIRouter, Depends

from api.authz.authorizer.paig_authorizer import AuthzRequest, AuthzResponse, VectorDBAuthzRequest, VectorDBAuthzResponse
from api.authz.controllers.paig_authorizer_controller import PAIGAuthorizerController

paig_authorizer_router = APIRouter()


@paig_authorizer_router.post("")
async def authorize(
        authz_request: AuthzRequest,
        paig_authorizer_controller: PAIGAuthorizerController = Depends(PAIGAuthorizerController)
) -> AuthzResponse:
    """
    Authorize the provided request.
    """
    return await paig_authorizer_controller.authorize(authz_request)


@paig_authorizer_router.post("/vectordb")
async def authorize(
        authz_request: VectorDBAuthzRequest,
        paig_authorizer_controller: PAIGAuthorizerController = Depends(PAIGAuthorizerController)
) -> VectorDBAuthzResponse:
    """
    Get vector db filter expression for the provided request.
    """
    return await paig_authorizer_controller.authorize_vector_db(authz_request)
