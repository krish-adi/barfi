# Usage: $ make {command}

.ONESHELL:

.PHONY: serve
serve: 
	cd frontend && npm run serve

.PHONY: run
run: 
	streamlit run st_barfi/__init__.py 
