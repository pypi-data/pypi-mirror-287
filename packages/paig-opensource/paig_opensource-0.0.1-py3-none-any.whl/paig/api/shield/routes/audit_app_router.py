from fastapi import APIRouter, Body, Depends
from typing import Annotated
from api.shield.controllers.shield_controller import ShieldController

audit_app_router = APIRouter()


@audit_app_router.post("")
async def audit(request: Annotated[dict | None, Body()],
                shield_controller: ShieldController = Depends(ShieldController)):
    """
       Handles POST requests to audit logs.

       This endpoint processes an audit request and delegates the task to the `ShieldController`
       to handle the audit logic.

       Returns:
           The result of the audit operation handled by `ShieldController`.
       """
    return await shield_controller.audit(request)
