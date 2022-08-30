# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Barfi'
copyright = '2022, Adithya Krishnan'
author = 'Adithya Krishnan'

# The short X.Y version.
version = '0.7.0'
# The full version, including alpha/beta/rc tags.
release = 'alpha'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.duration", "sphinx.ext.autodoc",
                "myst_parser", "sphinx_copybutton"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The file extensions of source files. Sphinx considers the files with this 
# suffix as sources. The value can be a dictionary mapping file extensions 
# to file types. For example:

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The “title” for HTML documentation generated with Sphinx’s own templates. 
# This is appended to the <title> tag of individual pages, and used in the 
# navigation bar as the “topmost” element. 
# It defaults to '<project> v<revision> documentation'.
html_title = 'Barfi'
html_short_title = 'Barfi - documentation'

# Navigation with keyboard keys
html_theme_options = {
    "navigation_with_keys": True,
}

# Footer configuration
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True


##### TODO: Set these #####
# # Logo
# html_logo = "logo.png"
# html_favicon = "favicon.png"
# # custom css
# html_css_files = [
#     'custom.css',
# ]