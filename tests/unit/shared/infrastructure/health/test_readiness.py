from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from sqlalchemy.exc import OperationalError

from geem_ai.shared.infrastructure.health.readiness import is_database_ready


def test_database_is_ready_when_revision_matches(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine = MagicMock()
    connection = engine.connect.return_value.__enter__.return_value

    revision_result = MagicMock()
    revision_result.scalar_one_or_none.return_value = "revision-1"

    connection.execute.side_effect = [
        MagicMock(),
        revision_result,
    ]

    monkeypatch.setattr(
        "geem_ai.shared.infrastructure.health.readiness.get_expected_database_revision",
        lambda: "revision-1",
    )

    assert is_database_ready(engine) is True


def test_database_is_not_ready_when_revision_differs(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine = MagicMock()
    connection = engine.connect.return_value.__enter__.return_value

    revision_result = MagicMock()
    revision_result.scalar_one_or_none.return_value = "old-revision"

    connection.execute.side_effect = [
        MagicMock(),
        revision_result,
    ]

    monkeypatch.setattr(
        "geem_ai.shared.infrastructure.health.readiness.get_expected_database_revision",
        lambda: "revision-1",
    )

    assert is_database_ready(engine) is False


def test_database_is_not_ready_when_connection_fails() -> None:
    engine = MagicMock()

    engine.connect.side_effect = OperationalError(
        statement=None,
        params=None,
        orig=Exception("database unavailable"),
    )

    assert is_database_ready(engine) is False
