# Usage: $ make {command}

.ONESHELL:

.PHONY: serve-ui
serve-ui: 
	cd ui-flow && npm run dev

.PHONY: build-ui
build-ui: 
	cd ui-flow && npm run build

.PHONY: serve-flow
serve-flow: 
	cd tests && poetry run streamlit run app.py 

.PHONY: ruff
ruff:
	poetry run ruff check src/barfi/flow/ && poetry run ruff format src/barfi/flow/ && \
	poetry run ruff check tests/ && poetry run ruff format tests/

.PHONY: tests
tests: 
	poetry run pytest tests -v -s

.PHONY: build-upload
build-upload:
	poetry publish --build --username __token__ --password $$BARFI_PYPI_KEY --skip-existing
