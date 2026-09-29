from datetime import UTC, datetime, timedelta
from uuid import UUID

from sqlalchemy import Engine, delete
from sqlalchemy.orm import Session

from geem_ai.conversations.application.idempotency import IdempotencyRecord
from geem_ai.conversations.infrastructure.persistence.models import IdempotencyRecordModel
from geem_ai.conversations.infrastructure.persistence.repositories import (
    SQLAlchemyIdempotencyRepository,
)
from geem_ai.shared.domain.ids import TenantId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import create_database_engine

NOW = datetime(2026, 9, 29, 12, tzinfo=UTC)
TENANT = TenantId(UUID("10000000-0000-0000-0000-000000000001"))
OTHER_TENANT = TenantId(UUID("20000000-0000-0000-0000-000000000001"))


def record(*, record_id: int, tenant: TenantId = TENANT) -> IdempotencyRecord:
    return IdempotencyRecord(
        id=UUID(int=record_id),
        tenant_id=tenant.value,
        scope="conversations.send-message",
        idempotency_key="same-key",
        request_hash="a" * 64,
        status="processing",
        response_status=None,
        response_body=None,
        resource_type=None,
        resource_id=None,
        created_at=NOW,
        completed_at=None,
        expires_at=NOW + timedelta(hours=24),
    )


def cleanup(engine: Engine) -> None:
    with Session(engine) as session:
        session.execute(delete(IdempotencyRecordModel))
        session.commit()


def test_idempotency_mapping_and_completion_persist_safe_response() -> None:
    engine = create_database_engine(get_settings().database_url)
    cleanup(engine)
    item = record(record_id=1)
    response = {
        "user_message_id": str(UUID(int=11)),
        "assistant_execution_id": str(UUID(int=12)),
        "execution_status": "created",
        "capability": "direct_response",
    }
    try:
        with Session(engine) as session:
            repository = SQLAlchemyIdempotencyRepository(session)
            assert repository.reserve(item) is True
            repository.complete(
                item,
                response_status=200,
                response_body=response,
                resource_type="assistant_execution",
                resource_id=UUID(int=12),
                completed_at=NOW,
            )
            session.commit()

        with Session(engine) as session:
            stored = session.get(IdempotencyRecordModel, UUID(int=1))
            assert stored is not None
            assert stored.status == "completed"
            assert stored.response_status == 200
            assert stored.response_body == response
            assert stored.completed_at == NOW
            assert stored.expires_at == NOW + timedelta(hours=24)
    finally:
        cleanup(engine)
        engine.dispose()


def test_atomic_reservation_is_tenant_scoped_and_does_not_raise_on_conflict() -> None:
    engine = create_database_engine(get_settings().database_url)
    cleanup(engine)
    try:
        with Session(engine) as session:
            repository = SQLAlchemyIdempotencyRepository(session)
            assert repository.reserve(record(record_id=1)) is True
            assert repository.reserve(record(record_id=2)) is False
            assert repository.reserve(record(record_id=3, tenant=OTHER_TENANT)) is True
            session.commit()
    finally:
        cleanup(engine)
        engine.dispose()


def test_completion_update_is_tenant_scoped() -> None:
    engine = create_database_engine(get_settings().database_url)
    cleanup(engine)
    stored = record(record_id=1)
    mismatched = record(record_id=1, tenant=OTHER_TENANT)
    try:
        with Session(engine) as session:
            repository = SQLAlchemyIdempotencyRepository(session)
            assert repository.reserve(stored) is True
            repository.complete(
                mismatched,
                response_status=200,
                response_body={"execution_status": "created"},
                resource_type="assistant_execution",
                resource_id=UUID(int=12),
                completed_at=NOW,
            )
            session.commit()

        with Session(engine) as session:
            persisted = session.get(IdempotencyRecordModel, stored.id)
            assert persisted is not None
            assert persisted.status == "processing"
            assert persisted.response_body is None
            assert persisted.completed_at is None
    finally:
        cleanup(engine)
        engine.dispose()


def test_rollback_removes_processing_record() -> None:
    engine = create_database_engine(get_settings().database_url)
    cleanup(engine)
    try:
        with Session(engine) as session:
            assert SQLAlchemyIdempotencyRepository(session).reserve(record(record_id=1)) is True
            session.rollback()

        with Session(engine) as session:
            assert session.get(IdempotencyRecordModel, UUID(int=1)) is None
    finally:
        cleanup(engine)
        engine.dispose()
