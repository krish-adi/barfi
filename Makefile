# Usage: $ make {command}

.ONESHELL:

.PHONY: serve
serve: 
	cd frontend && npm run serve

.PHONY: run
run: 
	cd tests && streamlit run test_app.py 

.PHONY: test
test: 
	cd tests/unittests && python -m unittest discover

.PHONY: upload
upload: 
	twine upload -u "__token__" -p "$(PYPI_BARFI_API)" --skip-existing --verbose dist/*
