lint:
	poetry run isort -rc pixivapi
	poetry run flake8 pixivapi

.PHONY: lint
