from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class TenantId:
    value: UUID


@dataclass(frozen=True, slots=True)
class UserId:
    value: UUID


@dataclass(frozen=True, slots=True)
class ConversationId:
    value: UUID


@dataclass(frozen=True, slots=True)
class MessageId:
    value: UUID


@dataclass(frozen=True, slots=True)
class ExecutionId:
    value: UUID
