.PHONY: install lint test security run docker-build docker-run

install:
	pip install -r requirements-dev.txt

lint:
	ruff check .

test:
	pytest --cov --cov-report=term-missing

security:
	bandit -r app
	pip-audit -r requirements.txt

run:
	python -m app.main

docker-build:
	docker build -t cicd-starter .

docker-run:
	docker run -p 5000:5000 cicd-starter
