lint:
	poetry run isort -rc pixivapi
	poetry run flake8 pixivapi

check:
	poetry run isort -rc -c .
	poetry run flake8
docs:
	rm -r _docs_build/*; poetry run sphinx-build -M html docs _docs_build

.PHONY: lint check docs
