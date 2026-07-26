FROM python:3.12.13-slim-bookworm@sha256:d50fb7611f86d04a3b0471b46d7557818d88983fc3136726336b2a4c657aa30b

ARG APP_UID=10001
ARG APP_GID=10001

ENV UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_PYTHON_DOWNLOADS=never \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

RUN groupadd --gid "${APP_GID}" app \
    && useradd \
        --uid "${APP_UID}" \
        --gid "${APP_GID}" \
        --create-home \
        --shell /usr/sbin/nologin \
        app

COPY pyproject.toml uv.lock .python-version README.md ./
COPY alembic.ini ./
COPY migrations ./migrations
COPY src ./src
COPY apps ./apps
COPY tests ./tests

RUN python -m pip install --no-cache-dir "uv==0.11.32" \
    && uv sync --locked --all-extras \
    && chown -R app:app /app /opt/venv

USER app

CMD ["uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
