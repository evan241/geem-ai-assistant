from __future__ import annotations

import json
from pathlib import Path

from apps.api.main import create_app

OUTPUT_PATH = Path("artifacts/openapi.json")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    app = create_app()
    schema = app.openapi()

    OUTPUT_PATH.write_text(
        json.dumps(schema, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
