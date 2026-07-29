from __future__ import annotations

from typing import Self

from sqlalchemy import Engine, text
from sqlalchemy.orm import Session

from geem_ai.conversations.application.ports.repositories import (
    ConversationRepository,
)
from geem_ai.conversations.infrastructure.persistence.repositories import (
    SQLAlchemyConversationRepository,
)
from geem_ai.shared.domain.actor import Actor


class SQLAlchemyConversationUnitOfWork:
    def __init__(
        self,
        *,
        engine: Engine,
        actor: Actor,
    ) -> None:
        self._engine = engine
        self._actor = actor
        self._committed = False

        self.session = Session(self._engine)
        self.conversations: ConversationRepository = SQLAlchemyConversationRepository(self.session)

    def __enter__(self) -> Self:
        self._set_actor_context()
        return self

    def __exit__(
        self,
        exc_type: object,
        exc_value: object,
        traceback: object,
    ) -> None:
        try:
            if exc_type is not None or not self._committed:
                self.rollback()
        finally:
            self.session.close()

    def commit(self) -> None:
        self.session.commit()
        self._committed = True

    def rollback(self) -> None:
        self.session.rollback()

    def _set_actor_context(self) -> None:
        self.session.execute(
            text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
            {
                "tenant_id": str(self._actor.tenant_id.value),
            },
        )

        self.session.execute(
            text("SELECT set_config('app.user_id', :user_id, true)"),
            {
                "user_id": (
                    str(self._actor.user_id.value) if self._actor.user_id is not None else ""
                ),
            },
        )


class SQLAlchemyConversationUnitOfWorkFactory:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def create(
        self,
        actor: Actor,
    ) -> SQLAlchemyConversationUnitOfWork:
        return SQLAlchemyConversationUnitOfWork(
            engine=self._engine,
            actor=actor,
        )
