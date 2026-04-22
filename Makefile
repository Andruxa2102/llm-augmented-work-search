.PHONY: setup run api pipeline test

setup:
	python -m venv .venv
	.venv/bin/pip install -e ".[dev]"
	.venv/bin/alembic init alembic
	@echo "✅ Env ready. Run: source .venv/bin/activate"

db-init:
	alembic revision --autogenerate -m "init"
	alembic upgrade head

run-api:
	uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

pipeline:
	python scripts/run_pipeline.py

test:
	python -m pytest tests/ -v
