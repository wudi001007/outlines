# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Outlines"
copyright = "2023, Normal Computing"
author = "Remi Louf"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ["_templates"]

source_suffix = {".rst": "restructuredtext"}

pygments_style = "nord-darker"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = ""
html_logo = "_static/logo.png"
html_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/normal-computing/outlines",  # required
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
    ]
}
