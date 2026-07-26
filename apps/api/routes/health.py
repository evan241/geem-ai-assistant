from __future__ import annotations

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.health.readiness import is_database_ready
from geem_ai.shared.infrastructure.persistence.connection import (
    create_database_engine,
)

router = APIRouter(
    prefix="/api/v1/health",
    tags=["system"],
)


@router.get("/live")
async def liveness() -> dict[str, str]:
    return {"status": "alive"}


@router.get("/ready")
def readiness() -> JSONResponse:
    settings = get_settings()
    engine = create_database_engine(
        settings.database_url,
        connect_timeout_seconds=2,
    )

    try:
        if not is_database_ready(engine):
            return JSONResponse(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                content={"status": "not_ready"},
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": "ready"},
        )
    finally:
        engine.dispose()
