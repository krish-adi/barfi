# Minimal makefile for Sphinx documentation
#

.ONESHELL:

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Rebuild Sphinx documentation on changes, with live-reload in the browser.
# This will start a server at http://127.0.0.1:8000 and start watching for changes 
# in the docs/ directory. When a change is detected in docs/, the documentation is 
# rebuilt and any open browser windows are reloaded automatically. 
# KeyboardInterrupt (ctrl+c) will stop the server.
livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: build
build:	
	make html

.PHONY: live-build
live-build:		
	sphinx-autobuild "$(SOURCEDIR)" build/live-html $(SPHINXOPTS) $(O)

.PHONY: serve
serve:	
	cd build/html && open ./index.html
