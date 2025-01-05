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
	poetry run ruff check src/barfi/flow/ && poetry run ruff format src/barfi/flow/

.PHONY: tests
tests: 
	poetry run pytest tests -v -s

.PHONY: build-upload
build-upload: 
	# twine upload -u "__token__" -p "$(PYPI_BARFI_API)" --skip-existing --verbose dist/*
	echo "Upload to PyPi"
