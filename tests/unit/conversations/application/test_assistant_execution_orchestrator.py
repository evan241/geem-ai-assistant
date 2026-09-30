import asyncio
from datetime import UTC, datetime
from typing import Self
from uuid import uuid4

from geem_ai.ai_runtime.infrastructure.fake_model_gateway import FakeModelGateway
from geem_ai.ai_runtime.public import ModelExecutionResult, ModelUsage
from geem_ai.conversations.application.execution_context import ModelExecutionRequestBuilder
from geem_ai.conversations.application.handlers import (
    ClaimAssistantExecutionHandler,
    CompleteAssistantExecutionHandler,
)
from geem_ai.conversations.application.orchestration import AssistantExecutionOrchestrator
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId

NOW = datetime(2026, 9, 30, 11, tzinfo=UTC)


class Executions:
    def __init__(self, execution: AssistantExecution, events: list[str]) -> None:
        self.execution = execution
        self.events = events

    def get_for_update(self, tenant_id, execution_id):  # type: ignore[no-untyped-def]
        self.events.append("execution lookup")
        return (
            self.execution
            if (tenant_id, execution_id) == (self.execution.tenant_id, self.execution.id)
            else None
        )

    def save(self, execution):  # type: ignore[no-untyped-def]
        self.events.append("execution save")


class Messages:
    def __init__(self, user_message: Message, events: list[str]) -> None:
        self.user_message = user_message
        self.events = events
        self.added = []  # type: ignore[var-annotated]

    def list_recent_for_execution(self, tenant_id, conversation_id, *, limit):  # type: ignore[no-untyped-def]
        self.events.append("context load")
        return (self.user_message,)

    def get_for_execution(self, tenant_id, conversation_id, message_id):  # type: ignore[no-untyped-def]
        return self.user_message

    def add(self, message):  # type: ignore[no-untyped-def]
        self.added.append(message)
        self.events.append("message add")


class Uow:
    def __init__(
        self, name: str, execution: AssistantExecution, message: Message, events: list[str]
    ) -> None:
        self.name = name
        self.executions = Executions(execution, events)
        self.messages = Messages(message, events)
        self.events = events
        self.active = False

    def __enter__(self) -> Self:
        self.active = True
        self.events.append(f"{self.name} enter")
        return self

    def __exit__(self, *args: object) -> None:
        self.active = False
        self.events.append(f"{self.name} exit")

    def commit(self) -> None:
        self.events.append(f"{self.name} commit")


class Factory:
    def __init__(self, uows: list[Uow]) -> None:
        self.uows = uows

    def create(self, actor):  # type: ignore[no-untyped-def]
        return self.uows.pop(0)


class TrackingGateway(FakeModelGateway):
    def __init__(
        self, result: ModelExecutionResult, all_uows: list[Uow], events: list[str]
    ) -> None:
        super().__init__(result)
        self.all_uows = all_uows
        self.events = events

    async def execute(self, request):  # type: ignore[no-untyped-def]
        assert not any(uow.active for uow in self.all_uows)
        self.events.append("gateway")
        return await super().execute(request)


def test_success_sequence_uses_exact_request_and_deterministic_message_id() -> None:
    events: list[str] = []
    actor = Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))
    execution = AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=actor.tenant_id,
        conversation_id=ConversationId(uuid4()),
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=NOW,
    )
    user_message = Message.create_user(
        message_id=execution.user_message_id,
        conversation_id=execution.conversation_id,
        tenant_id=actor.tenant_id,
        author_id=actor.user_id,
        content="Question",
        now=NOW,  # type: ignore[arg-type]
    )
    uows = [
        Uow("claim", execution, user_message, events),
        Uow("context", execution, user_message, events),
        Uow("complete", execution, user_message, events),
    ]
    all_uows = list(uows)
    factory = Factory(uows)
    model_result = ModelExecutionResult(
        "Answer", "fake", "fake-model", ModelUsage(2, 3, 5), "stop", 10, 0.01
    )
    gateway = TrackingGateway(model_result, all_uows, events)
    message_id = MessageId(uuid4())
    orchestrator = AssistantExecutionOrchestrator(
        unit_of_work_factory=factory,  # type: ignore[arg-type]
        claim_handler=ClaimAssistantExecutionHandler(
            unit_of_work_factory=factory, clock=lambda: NOW
        ),  # type: ignore[arg-type]
        request_builder=ModelExecutionRequestBuilder(),
        model_gateway=gateway,
        complete_handler=CompleteAssistantExecutionHandler(
            unit_of_work_factory=factory, clock=lambda: NOW
        ),  # type: ignore[arg-type]
        fail_handler=None,  # type: ignore[arg-type]
        message_id_factory=lambda: message_id,
    )

    asyncio.run(orchestrator.execute(actor=actor, execution_id=execution.id))

    assert len(gateway.requests) == 1
    assert gateway.requests[0].tenant_id == actor.tenant_id
    assert gateway.requests[0].execution_id == execution.id
    assert gateway.requests[0].capability == "direct_response"
    assert gateway.requests[0].messages[0].content == "Question"
    assert events.index("claim commit") < events.index("claim exit") < events.index("context enter")
    assert events.index("context load") < events.index("context exit") < events.index("gateway")
    assert events.index("gateway") < events.index("complete enter")
    assert execution.assistant_message_id == message_id
