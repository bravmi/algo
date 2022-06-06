
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
