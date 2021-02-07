docs:
	rm -rf docs/_build/html docs/_build/doctrees
	poetry run sphinx-build -M html docs docs/_build

tests:
	poetry run pytest --cov=. --cov-branch tests/

lint:
	poetry run black .
	poetry run isort .
	poetry run flake8 .

lintcheck:
	poetry run black --check .
	poetry run isort -c .
	poetry run flake8 .

setup.py:
	poetry run dephell deps convert --from pyproject.toml --to setup.py

setupcheck:
	mv setup.py setup.py.old
	make setup.py
	diff setup.py.old setup.py
	rm setup.py.old

.PHONY: docs tests lint lintcheck setup.py setupcheck
