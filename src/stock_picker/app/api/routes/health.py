from fastapi import APIRouter, Depends
from ...dependencies import get_health_service
from ...services import HealthService

router = APIRouter(tags=["health"])


@router.get("/healthz")
def healthcheck(service: HealthService = Depends(get_health_service)) -> dict[str, str]:
    return service.get_status()
