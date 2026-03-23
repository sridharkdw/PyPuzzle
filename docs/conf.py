import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "PyPuzzle"
author = "PyPuzzle"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

html_theme = "sphinx_rtd_theme"
html_static_path = []
