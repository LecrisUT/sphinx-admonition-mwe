project = 'Sphinx MWE'
copyright = '2023, Cristian Le'
author = 'Cristian Le'

extensions = [
    "myst_parser",
    "sphinx_design",
]

myst_enable_extensions = [
    "colon_fence",
]

html_theme = 'furo'
templates_path = []
source_suffix = [".md"]
exclude_patterns = [
    "admonition.md",
]
