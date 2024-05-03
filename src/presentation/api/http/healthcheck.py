from fastapi import APIRouter, status
from dataclasses import dataclass

healthcheck_router = APIRouter(prefix="/healthcheck", tags=["healthcheck"])


@dataclass(frozen=True)
class OkStatus:
    status: str = "OK"


OK_STATUS = OkStatus()


@healthcheck_router.get(path="/", status_code=status.HTTP_200_OK)
async def get_status() -> OkStatus:
    return OK_STATUS
