FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY alembic.ini ./
COPY migrations ./migrations
COPY src ./src
COPY apps ./apps
COPY tests ./tests

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -e ".[dev]"

CMD ["uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
