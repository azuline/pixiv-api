lint:
	poetry run isort -rc pixivapi
	poetry run flake8 pixivapi

check:
	poetry run isort -rc -c .
	poetry run flake8

.PHONY: lint check
