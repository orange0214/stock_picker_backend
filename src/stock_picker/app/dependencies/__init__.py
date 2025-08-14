from __future__ import annotations

from typing import Generator

from ..services import HealthService


def get_health_service() -> Generator[HealthService, None, None]:
    service = HealthService()
    try:
        yield service
    finally:
        pass


__all__ = ["get_health_service"]
