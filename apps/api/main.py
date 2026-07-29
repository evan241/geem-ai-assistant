from fastapi import FastAPI

from apps.api.routes.health import router as health_router
from geem_ai.conversations.presentation.router import router as conversations_router
from geem_ai.shared.infrastructure.configuration.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
    )

    app.include_router(health_router)
    app.include_router(conversations_router)

    return app


app = create_app()
