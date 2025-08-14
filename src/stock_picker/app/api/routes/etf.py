from fastapi import APIRouter, Depends
from ...dependencies import get_etf_service
from ...services import ETFService

router = APIRouter(tags=["etf"])

@router.get("/etf")
def get_etf(service: ETFService = Depends(get_etf_service)) -> dict[str, str]:
    return service.get_etf()
