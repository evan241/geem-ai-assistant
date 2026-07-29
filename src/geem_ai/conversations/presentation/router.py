from __future__ import annotations

from typing import Annotated

from apps.api.dependencies.auth import get_actor
from apps.api.dependencies.conversations import (
    get_create_conversation_handler,
)
from fastapi import APIRouter, Depends, status

from geem_ai.conversations.application.commands import (
    CreateConversationCommand,
)
from geem_ai.conversations.application.handlers import (
    CreateConversationHandler,
)
from geem_ai.conversations.presentation.schemas import (
    ConversationResponse,
    CreateConversationRequest,
)
from geem_ai.shared.domain.actor import Actor

router = APIRouter(
    prefix="/api/v1/conversations",
    tags=["conversations"],
)


@router.post(
    "",
    response_model=ConversationResponse,
    status_code=status.HTTP_201_CREATED,
    operation_id="create_conversation",
    summary="Create a conversation",
)
def create_conversation(
    request: CreateConversationRequest,
    actor: Annotated[Actor, Depends(get_actor)],
    handler: Annotated[
        CreateConversationHandler,
        Depends(get_create_conversation_handler),
    ],
) -> ConversationResponse:
    result = handler.handle(
        CreateConversationCommand(
            actor=actor,
            title=request.title,
            language=request.language,
        )
    )

    return ConversationResponse(
        id=str(result.conversation_id.value),
        title=result.title,
        status=result.status,
        language=result.language,
        created_at=result.created_at,
        updated_at=result.updated_at,
    )
