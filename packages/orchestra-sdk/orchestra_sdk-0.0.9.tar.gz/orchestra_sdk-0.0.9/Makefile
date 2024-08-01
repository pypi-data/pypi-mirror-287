clean:
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf

install:
	pip install pip-tools
	pip-compile pyproject.toml
	pip-sync

install-dev:
	pip install pip-tools
	pip-compile --extra dev -o requirements-dev.txt pyproject.toml
	pip-sync requirements-dev.txt

format:
	ruff format .
	black .

lint: pyright-lint ruff-lint black-lint

pyright-lint:
	pyright

lint-fix: ruff-lint-fix black-lint-fix

ruff-lint:
	ruff check .

ruff-lint-fix:
	ruff --fix .

black-lint:
	black --check .

black-lint-fix:
	black .

unit:
	pytest

test-last-failed:
	pytest --last-failed -q

test: lint unit

build:
	rm -rf dist
	python -m build
	twine check dist/*

release-test:
	twine upload -r testpypi --config-file .pypirc dist/*

release:
	twine upload --config-file .pypirc dist/*

.PHONY: clean install install-dev format lint pyright-lint lint-fix ruff-lint ruff-lint-fix black-lint black-lint-fix unit test test-last-failed