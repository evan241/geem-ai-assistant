from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class CreateConversationRequest(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    language: Literal["es", "en"] = "es"


class ConversationResponse(BaseModel):
    id: str
    title: str
    status: Literal["active", "archived", "locked", "deleted"]
    language: Literal["es", "en"]
    created_at: datetime
    updated_at: datetime


class SendConversationMessageRequest(BaseModel):
    content: str = Field(min_length=1, max_length=32_000)
    response_mode: Literal["stream"] = "stream"
    capability_hint: Literal["direct_response"] | None = None


class SendConversationMessageResponse(BaseModel):
    user_message_id: str
    assistant_execution_id: str
    execution_status: Literal["created"]
    capability: Literal["direct_response"]
