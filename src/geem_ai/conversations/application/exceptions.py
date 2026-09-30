class ConversationNotFoundError(Exception):
    """Raised when a conversation is not found or is not visible."""


class AssistantExecutionNotFoundError(Exception):
    """Raised when an assistant execution is not found or is not visible."""


class AssistantExecutionNotClaimableError(Exception):
    """Raised when an assistant execution job has already been claimed or handled."""


class ExecutionUserMessageNotFoundError(Exception):
    """Raised when an execution's user message is absent from its tenant conversation."""


class UnsupportedExecutionCapabilityError(Exception):
    """Raised when orchestration does not support an execution capability."""


class InvalidIdempotencyKeyError(ValueError):
    """Raised when an idempotency key is empty or exceeds its storage limit."""


class IdempotencyKeyConflictError(Exception):
    """Raised when an idempotency key is reused for a different logical request."""


class IdempotencyRequestInProgressError(Exception):
    """Raised when an identical request using the key is still processing."""
