from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy import Engine

from geem_ai.ai_runtime.public import ModelGateway
from geem_ai.conversations.application.events import (
    ASSISTANT_EXECUTION_REQUESTED,
    OutboxEvent,
)
from geem_ai.conversations.application.execution_context import ModelExecutionRequestBuilder
from geem_ai.conversations.application.handlers import (
    ClaimAssistantExecutionHandler,
    CompleteAssistantExecutionHandler,
    FailAssistantExecutionHandler,
)
from geem_ai.conversations.application.orchestration import (
    AssistantExecutionJobHandler,
    AssistantExecutionOrchestrator,
)
from geem_ai.conversations.infrastructure.persistence.unit_of_work import (
    SQLAlchemyConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ExecutionId, MessageId, TenantId


class UnsupportedWorkerEventError(ValueError):
    """The delivered event contract is not supported by this adapter."""


class InvalidWorkerEventPayloadError(ValueError):
    """The delivered event cannot safely identify a tenant execution."""


class AssistantExecutionRequestedEventHandler:
    """Adapt an already-delivered event; transport and publishing live elsewhere."""

    def __init__(self, *, job_handler: AssistantExecutionJobHandler) -> None:
        self._job_handler = job_handler

    async def handle(self, event: OutboxEvent) -> None:
        execution_id = self._validate(event)
        assert event.tenant_id is not None
        actor = Actor.worker(tenant_id=TenantId(event.tenant_id))
        await self._job_handler.handle(actor=actor, execution_id=execution_id)

    @staticmethod
    def _validate(event: OutboxEvent) -> ExecutionId:
        if event.event_type != ASSISTANT_EXECUTION_REQUESTED:
            raise UnsupportedWorkerEventError(f"Unsupported worker event: {event.event_type}.")
        if event.event_version != 1:
            raise UnsupportedWorkerEventError(
                f"Unsupported {ASSISTANT_EXECUTION_REQUESTED} version: {event.event_version}."
            )
        if event.tenant_id is None:
            raise InvalidWorkerEventPayloadError("Worker event tenant_id is required.")
        if event.aggregate_type != "assistant_execution":
            raise InvalidWorkerEventPayloadError(
                "Worker event aggregate_type must be assistant_execution."
            )

        raw_execution_id = event.payload.get("assistant_execution_id")
        if not isinstance(raw_execution_id, str):
            raise InvalidWorkerEventPayloadError(
                "Worker event assistant_execution_id must be a UUID string."
            )
        try:
            parsed_execution_id = UUID(raw_execution_id)
        except ValueError as error:
            raise InvalidWorkerEventPayloadError(
                "Worker event assistant_execution_id must be a valid UUID."
            ) from error
        if parsed_execution_id != event.aggregate_id:
            raise InvalidWorkerEventPayloadError(
                "Worker event aggregate_id does not match assistant_execution_id."
            )
        return ExecutionId(parsed_execution_id)


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _new_message_id() -> MessageId:
    return MessageId(uuid4())


def build_assistant_execution_job_handler(
    *, engine: Engine, model_gateway: ModelGateway
) -> AssistantExecutionJobHandler:
    """Compose the assistant execution application slice for a future transport."""
    unit_of_work_factory = SQLAlchemyConversationUnitOfWorkFactory(engine)
    orchestrator = AssistantExecutionOrchestrator(
        unit_of_work_factory=unit_of_work_factory,
        claim_handler=ClaimAssistantExecutionHandler(
            unit_of_work_factory=unit_of_work_factory,
            clock=_utc_now,
        ),
        request_builder=ModelExecutionRequestBuilder(),
        model_gateway=model_gateway,
        complete_handler=CompleteAssistantExecutionHandler(
            unit_of_work_factory=unit_of_work_factory,
            clock=_utc_now,
        ),
        fail_handler=FailAssistantExecutionHandler(
            unit_of_work_factory=unit_of_work_factory,
            clock=_utc_now,
        ),
        message_id_factory=_new_message_id,
    )
    return AssistantExecutionJobHandler(orchestrator)
