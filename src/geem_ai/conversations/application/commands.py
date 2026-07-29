from __future__ import annotations

from dataclasses import dataclass

from geem_ai.shared.domain.actor import Actor


@dataclass(frozen=True, slots=True)
class CreateConversationCommand:
    actor: Actor
    title: str | None
    language: str
    idempotency_key: str | None = None
