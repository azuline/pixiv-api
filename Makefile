lint:
	poetry run isort -rc pixivapi
	poetry run flake8 pixivapi

check:
	poetry run isort -rc -c .
	poetry run flake8
docs:
	rm -r docs/_build/html docs/_build/doctrees
	poetry run sphinx-build -M html docs docs/_build

.PHONY: lint check docs
