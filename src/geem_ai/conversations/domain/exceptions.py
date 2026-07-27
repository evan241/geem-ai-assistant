class ConversationDomainError(Exception):
    """Base exception for conversation domain errors."""


class ConversationNotActiveError(ConversationDomainError):
    """Raised when a conversation cannot accept new messages."""


class MessageContentLockedError(ConversationDomainError):
    """Raised when completed message content is modified."""


class AssistantExecutionDomainError(ConversationDomainError):
    """Base exception for assistant execution domain errors."""


class InvalidExecutionTransitionError(AssistantExecutionDomainError):
    """Raised when an assistant execution transition is invalid."""


class MissingExecutionResultError(AssistantExecutionDomainError):
    """Raised when a completed execution has no result."""


class MissingExecutionFailureError(AssistantExecutionDomainError):
    """Raised when a failed execution has no failure information."""


class NegativeExecutionMetricError(AssistantExecutionDomainError):
    """Raised when execution metrics contain negative values."""
