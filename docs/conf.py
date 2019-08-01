# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Path setup

import os
import sys

sys.path.insert(0, os.path.abspath('.'))


# -- Project information

project = 'pixiv-api'
copyright = '2019, azuline'
author = 'azuline'
release = '0.0.1'

# -- General configuration

extensions = ['sphinx.ext.autodoc']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'
master_doc = 'index'

# -- Options for HTML output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Extension configuration

autodoc_default_options = {'member-order': 'bysource'}
