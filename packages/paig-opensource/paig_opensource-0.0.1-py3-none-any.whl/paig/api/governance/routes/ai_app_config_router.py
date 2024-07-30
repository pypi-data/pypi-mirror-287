from fastapi import APIRouter, Depends

from api.governance.api_schemas.ai_app_config import AIApplicationConfigView
from api.governance.controllers.ai_app_config_controller import AIAppConfigController

ai_app_config_router = APIRouter()


@ai_app_config_router.get("/config", response_model=AIApplicationConfigView)
async def get_application_config(
        id: int,
        ai_app_config_controller: AIAppConfigController = Depends(AIAppConfigController)
) -> AIApplicationConfigView:
    """
    Get the configuration of an AI application by ID.
    """
    return await ai_app_config_controller.get_ai_app_config(id)


@ai_app_config_router.put("/config", response_model=AIApplicationConfigView)
async def update_application_config(
        id: int,
        update_ai_app_config_request: AIApplicationConfigView,
        ai_app_config_controller: AIAppConfigController = Depends(AIAppConfigController)
) -> AIApplicationConfigView:
    """
    Update the configuration of an AI application by ID.
    """
    return await ai_app_config_controller.update_ai_app_config(id, update_ai_app_config_request)
