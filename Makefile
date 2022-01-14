# Usage: $ make {command}

.ONESHELL:

.PHONY: serve
serve: 
	cd st_barfi/frontend && npm run serve

.PHONY: run
run: 
	streamlit run st_barfi/__init__.py 
