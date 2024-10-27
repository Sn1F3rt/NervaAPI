env:
	uv venv

prod:
	uv sync --no-dev

dev:
	uv sync --all-extras

format:
	ruff check --select I --fix .
	ruff format .

run:
	uv run launcher.py

.PHONY: env dev format run
.DEFAULT_GOAL := run
