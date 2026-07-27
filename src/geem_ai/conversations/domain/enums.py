from enum import StrEnum


class ConversationStatus(StrEnum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    LOCKED = "locked"
    DELETED = "deleted"


class MessageRole(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


class MessageStatus(StrEnum):
    PENDING = "pending"
    STREAMING = "streaming"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REDACTED = "redacted"


class ExecutionStatus(StrEnum):
    CREATED = "created"
    RUNNING = "running"
    WAITING_FOR_APPROVAL = "waiting_for_approval"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"


class ExecutionCapability(StrEnum):
    DIRECT_RESPONSE = "direct_response"
    KNOWLEDGE_QUERY = "knowledge_query"
    TOOL_REQUEST = "tool_request"
    MEMORY_OPERATION = "memory_operation"
    WORKFLOW = "workflow"


class ConversationLanguage(StrEnum):
    ES = "es"
    EN = "en"
