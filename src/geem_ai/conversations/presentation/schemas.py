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
