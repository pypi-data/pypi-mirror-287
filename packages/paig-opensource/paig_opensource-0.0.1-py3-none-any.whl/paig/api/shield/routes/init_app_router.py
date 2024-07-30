from fastapi import APIRouter, Request, Depends

from api.shield.controllers.shield_controller import ShieldController

init_app_router = APIRouter()


@init_app_router.post("")
async def init_app(request: Request, shield_controller: ShieldController = Depends(ShieldController)):
    """
    Handles POST requests to initialize an application.

    This endpoint processes a request to initialize the application and delegates
    the task to the `ShieldController` to perform the initialization logic.

    Returns:
        The result of the application initialization operation handled by `ShieldController`.
    """
    return await shield_controller.init_app(request)
