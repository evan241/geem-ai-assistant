from __future__ import annotations

from typing import Annotated, Literal, cast
from uuid import UUID

from apps.api.dependencies.auth import get_actor
from apps.api.dependencies.conversations import (
    get_create_conversation_handler,
    get_get_conversation_handler,
    get_send_conversation_message_handler,
)
from fastapi import APIRouter, Depends, Header, HTTPException, status

from geem_ai.conversations.application.commands import (
    CreateConversationCommand,
    SendConversationMessageCommand,
)
from geem_ai.conversations.application.exceptions import (
    ConversationNotFoundError,
    IdempotencyKeyConflictError,
    IdempotencyRequestInProgressError,
    InvalidIdempotencyKeyError,
)
from geem_ai.conversations.application.handlers import (
    CreateConversationHandler,
    GetConversationHandler,
    SendConversationMessageHandler,
)
from geem_ai.conversations.application.queries import GetConversationQuery
from geem_ai.conversations.domain.exceptions import (
    ConversationNotActiveError,
    InvalidMessageContentError,
)
from geem_ai.conversations.presentation.schemas import (
    ConversationResponse,
    CreateConversationRequest,
    SendConversationMessageRequest,
    SendConversationMessageResponse,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId

router = APIRouter(
    prefix="/api/v1/conversations",
    tags=["conversations"],
)


@router.post(
    "/{conversation_id}/messages",
    response_model=SendConversationMessageResponse,
    status_code=status.HTTP_202_ACCEPTED,
    operation_id="send_conversation_message",
    summary="Accept a conversation message",
)
def send_conversation_message(
    conversation_id: UUID,
    request: SendConversationMessageRequest,
    actor: Annotated[Actor, Depends(get_actor)],
    handler: Annotated[
        SendConversationMessageHandler,
        Depends(get_send_conversation_message_handler),
    ],
    idempotency_key: Annotated[
        str,
        Header(alias="Idempotency-Key", min_length=1, max_length=255),
    ],
) -> SendConversationMessageResponse:
    try:
        result = handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=ConversationId(conversation_id),
                content=request.content,
                capability_hint=request.capability_hint,
                idempotency_key=idempotency_key,
            )
        )
    except ConversationNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.",
        ) from error
    except ConversationNotActiveError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conversation is not active.",
        ) from error
    except InvalidMessageContentError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Message content is invalid.",
        ) from error
    except InvalidIdempotencyKeyError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Idempotency key is invalid.",
        ) from error
    except IdempotencyKeyConflictError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Idempotency key conflicts with another request.",
        ) from error
    except IdempotencyRequestInProgressError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A request with this idempotency key is still processing.",
        ) from error

    return SendConversationMessageResponse(
        user_message_id=str(result.user_message_id.value),
        assistant_execution_id=str(result.assistant_execution_id.value),
        execution_status=cast(Literal["created"], result.execution_status),
        capability=cast(Literal["direct_response"], result.capability),
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
