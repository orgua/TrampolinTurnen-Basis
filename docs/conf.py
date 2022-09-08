# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#project = 'Einführung ins Trampolinturnen'
project = 'Trampolinturnen'
copyright = '2022, Ingmar Splitt'
author = 'Ingmar Splitt'
release = '0.3'  # TODO: change to date
builder = "html latexpdf"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxawesome_theme",
    "sphinx_sitemap",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Einführung in das Trampolinturnen"
html_collapsible_definitions = True
html_copy_source = False

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_theme_options = {
    "show_scrolltop": True,
    "show_prev_next": True,
    "extra_header_links": {
        "PDF-Version": "https://github.com/orgua/TrampolinTurnen-Basis/releases",
        "Quelldateien": "https://github.com/orgua/TrampolinTurnen-Basis/tree/main/docs/content",
    },
}
# TODO: https://sphinxawesome.xyz/how-to/options/
html_baseurl = 'https://orgua.github.io/TrampolinTurnen-Basis/'
html_extra_path = ['robots.txt']
html_static_path = ['_static']

sitemap_url_scheme = "{link}"

# -- Options for LATEX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/latex.html

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "14pt",
    "fncychap": '',  # '\\usepackage[Bjornstrup]{fncychap}',
    "transition": "\\bigskip"
}

#latex_docclass = {
#    'manual': 'report',
#}

