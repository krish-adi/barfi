# Usage: $ make {command}

.ONESHELL:

.PHONY: serve
serve: 
	cd frontend && npm run serve

.PHONY: run
run: 
	cd tests && streamlit run test_app.py 
