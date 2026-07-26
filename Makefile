up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

test:
	docker compose run --rm api pytest

lint:
	docker compose run --rm api ruff check .
	docker compose run --rm web pnpm lint

format:
	docker compose run --rm api ruff format .
	docker compose run --rm web pnpm format

typecheck:
	docker compose run --rm api mypy src apps
	docker compose run --rm web pnpm typecheck

migration:
	docker compose run --rm api alembic revision --autogenerate -m "$(m)"

migrate:
	docker compose run --rm api alembic upgrade head

migration-current:
	docker compose run --rm api alembic current

migration-heads:
	docker compose run --rm api alembic heads