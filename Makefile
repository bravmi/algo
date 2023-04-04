.PHONY: *

cov:
	pytest --cov=. --cov-report=html --no-cov-on-fail

test:
	pytest .

lint:
	make flake8
	make mypy

flake8:
	flake8 .

mypy:
	mypy .

fmt:
	make black
	make isort

black:
	black .

isort:
	isort .

update:
	poetry update -vv
	poetry export --format requirements.txt --output requirements.txt --dev

build:
	act --job build
