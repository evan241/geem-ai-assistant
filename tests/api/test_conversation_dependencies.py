import pytest
from apps.api.dependencies import conversations

from geem_ai.conversations.application.handlers import SendConversationMessageHandler


class FakeEngine:
    def __init__(self) -> None:
        self.disposed = False

    def dispose(self) -> None:
        self.disposed = True


def test_send_message_dependency_wires_handler_and_disposes_engine(monkeypatch) -> None:
    engine = FakeEngine()
    monkeypatch.setattr(conversations, "create_database_engine", lambda _url: engine)
    dependency = conversations.get_send_conversation_message_handler()

    handler = next(dependency)

    assert isinstance(handler, SendConversationMessageHandler)
    assert handler._message_id_factory() != handler._message_id_factory()
    assert handler._execution_id_factory() != handler._execution_id_factory()
    assert handler._idempotency_id_factory() != handler._idempotency_id_factory()
    assert handler._outbox_event_id_factory() != handler._outbox_event_id_factory()
    assert handler._clock().tzinfo is not None

    with pytest.raises(StopIteration):
        next(dependency)

    assert engine.disposed is True
