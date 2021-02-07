# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Path setup

import os
import sys

sys.path.insert(0, os.path.abspath("../"))


# -- Project information

project = "pixiv-api"
copyright = "2021, blissful"
author = "blissful"
release = "0.3.7"

# -- General configuration

extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
master_doc = "index"

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
