from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class HealthService:
    def get_status(self) -> dict[str, str]:
        return {"status": "ok", "time": datetime.utcnow().isoformat() + "Z"}
