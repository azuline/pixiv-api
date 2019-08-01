lint:
	poetry run yapf --in-place --verbose --parallel --recursive .
	poetry run isort -rc pixivapi
	poetry run flake8 pixivapi

check:
	poetry run yapf --parallel --diff --recursive .
	poetry run isort -rc -c .
	poetry run flake8

.PHONY: lint check
