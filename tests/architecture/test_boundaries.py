from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = PROJECT_ROOT / "src" / "geem_ai"

LAYER_NAMES = {
    "domain",
    "application",
    "infrastructure",
    "presentation",
}

BOUNDED_CONTEXTS = {
    "administration",
    "ai_runtime",
    "approvals",
    "audit",
    "conversations",
    "evaluation",
    "identity",
    "knowledge",
    "memory",
    "observability",
    "organizations",
    "retrieval",
    "tools",
}

DOMAIN_FORBIDDEN_PACKAGES = {
    "alembic",
    "anthropic",
    "boto3",
    "botocore",
    "fastapi",
    "httpx",
    "openai",
    "opentelemetry",
    "psycopg",
    "redis",
    "sqlalchemy",
}

APPLICATION_FORBIDDEN_PACKAGES = {
    "fastapi",
}


@dataclass(frozen=True)
class ImportReference:
    file: Path
    module: str
    line: int


def _python_files() -> list[Path]:
    return sorted(SOURCE_ROOT.rglob("*.py"))


def _imports_from_file(file: Path) -> list[ImportReference]:
    tree = ast.parse(file.read_text(encoding="utf-8"), filename=str(file))
    imports: list[ImportReference] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(
                    ImportReference(
                        file=file,
                        module=alias.name,
                        line=node.lineno,
                    )
                )

        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imports.append(
                ImportReference(
                    file=file,
                    module=node.module,
                    line=node.lineno,
                )
            )

    return imports


def _all_imports() -> list[ImportReference]:
    return [imported for file in _python_files() for imported in _imports_from_file(file)]


def _relative_parts(file: Path) -> tuple[str, ...]:
    return file.relative_to(SOURCE_ROOT).parts


def _layer_for(file: Path) -> str | None:
    parts = _relative_parts(file)

    for part in parts:
        if part in LAYER_NAMES:
            return part

    return None


def _bounded_context_for(file: Path) -> str | None:
    parts = _relative_parts(file)

    if not parts:
        return None

    context = parts[0]

    if context in BOUNDED_CONTEXTS:
        return context

    return None


def _top_level_package(module: str) -> str:
    return module.split(".", maxsplit=1)[0]


def _format_violation(imported: ImportReference, reason: str) -> str:
    relative_file = imported.file.relative_to(PROJECT_ROOT)

    return (
        f"{relative_file}:{imported.line}: "
        f"{imported.module!r} violates architecture boundary: {reason}"
    )


def test_domain_does_not_depend_on_forbidden_infrastructure_packages() -> None:
    violations: list[str] = []

    for imported in _all_imports():
        if _layer_for(imported.file) != "domain":
            continue

        package = _top_level_package(imported.module)

        if package in DOMAIN_FORBIDDEN_PACKAGES:
            violations.append(
                _format_violation(
                    imported,
                    f"domain must not depend on {package!r}",
                )
            )

    assert not violations, "\n" + "\n".join(violations)


def test_domain_does_not_import_infrastructure_or_presentation_layers() -> None:
    violations: list[str] = []

    for imported in _all_imports():
        if _layer_for(imported.file) != "domain":
            continue

        parts = imported.module.split(".")

        if "infrastructure" in parts or "presentation" in parts:
            violations.append(
                _format_violation(
                    imported,
                    "domain must not import infrastructure or presentation",
                )
            )

    assert not violations, "\n" + "\n".join(violations)


def test_application_does_not_import_presentation_or_fastapi() -> None:
    violations: list[str] = []

    for imported in _all_imports():
        if _layer_for(imported.file) != "application":
            continue

        package = _top_level_package(imported.module)
        parts = imported.module.split(".")

        if package in APPLICATION_FORBIDDEN_PACKAGES:
            violations.append(
                _format_violation(
                    imported,
                    f"application must not depend on {package!r}",
                )
            )

        if "presentation" in parts:
            violations.append(
                _format_violation(
                    imported,
                    "application must not import presentation",
                )
            )

    assert not violations, "\n" + "\n".join(violations)


def test_bounded_contexts_only_use_other_modules_public_api() -> None:
    violations: list[str] = []

    for imported in _all_imports():
        source_context = _bounded_context_for(imported.file)

        if source_context is None:
            continue

        parts = imported.module.split(".")

        if len(parts) < 2 or parts[0] != "geem_ai":
            continue

        target_context = parts[1]

        if target_context == "shared":
            continue

        if target_context not in BOUNDED_CONTEXTS:
            continue

        if target_context == source_context:
            continue

        expected_public_module = f"geem_ai.{target_context}.public"

        if imported.module != expected_public_module:
            violations.append(
                _format_violation(
                    imported,
                    (
                        f"{source_context!r} may consume {target_context!r} "
                        f"only through {expected_public_module!r}"
                    ),
                )
            )

    assert not violations, "\n" + "\n".join(violations)
