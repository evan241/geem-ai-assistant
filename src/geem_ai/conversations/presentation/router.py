from __future__ import annotations

from typing import Annotated
from uuid import UUID

from apps.api.dependencies.auth import get_actor
from apps.api.dependencies.conversations import (
    get_create_conversation_handler,
    get_get_conversation_handler,
)
from fastapi import APIRouter, Depends, HTTPException, status

from geem_ai.conversations.application.commands import (
    CreateConversationCommand,
)
from geem_ai.conversations.application.exceptions import ConversationNotFoundError
from geem_ai.conversations.application.handlers import (
    CreateConversationHandler,
    GetConversationHandler,
)
from geem_ai.conversations.application.queries import GetConversationQuery
from geem_ai.conversations.presentation.schemas import (
    ConversationResponse,
    CreateConversationRequest,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId

router = APIRouter(
    prefix="/api/v1/conversations",
    tags=["conversations"],
)


@router.get(
    "/{conversation_id}",
    response_model=ConversationResponse,
    status_code=status.HTTP_200_OK,
    operation_id="get_conversation",
    summary="Get a conversation",
)
def get_conversation(
    conversation_id: UUID,
    actor: Annotated[Actor, Depends(get_actor)],
    handler: Annotated[
        GetConversationHandler,
        Depends(get_get_conversation_handler),
    ],
) -> ConversationResponse:
    try:
        conversation = handler.handle(
            GetConversationQuery(
                actor=actor,
                conversation_id=ConversationId(conversation_id),
            )
        )
    except ConversationNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.",
        ) from error

    return ConversationResponse(
        id=str(conversation.conversation_id.value),
        title=conversation.title,
        status=conversation.status,
        language=conversation.language,
        created_at=conversation.created_at,
        updated_at=conversation.updated_at,
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
