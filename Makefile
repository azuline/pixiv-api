lint:
	isort -rc pixivapi
	flake8 pixivapi

check:
	isort -rc -c .
	flake8

docs:
	rm -rf docs/_build/html docs/_build/doctrees
	sphinx-build -M html docs docs/_build

.PHONY: lint check docs
