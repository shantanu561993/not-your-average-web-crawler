#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# N.Y.A.W.C documentation build configuration file, created by
# sphinx-quickstart on Fri May 12 17:22:14 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.napoleon',
    'sphinx.ext.linkcode',
    'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'N.Y.A.W.C'
copyright = '2017, Tijme Gommers'
author = 'Tijme Gommers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

with open("../../.semver") as file:
    semver = file.read()

# The short X.Y version.
version = semver
# The full version, including alpha/beta/rc tags.
release = semver

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
from better import better_theme_path
html_theme_path = [better_theme_path]
html_theme = 'better'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  # show sidebar on the right instead of on the left
  'rightsidebar': False,

  # CSS files to include after all other CSS files
  # (refer to by relative path from conf.py directory, or link to a
  # remote file)
  # 'cssfiles': ['_static/my_style.css'],  # default is empty list

  # show a big text header with the value of html_title
  'showheader': True,

  # show the breadcrumbs and index|next|previous links at the top of
  # the page
  'showrelbartop': True,
  # same for bottom of the page
  'showrelbarbottom': False,

  # show the self-serving link in the footer
  'linktotheme': False,

  # width of the sidebar. page width is determined by a CSS rule.
  # I prefer to define things in rem because it scales with the
  # global font size rather than pixels or the local font size.
  'sidebarwidth': '15rem',

  # color of all body text
  'textcolor': '#000000',

  # color of all headings (<h1> tags); defaults to the value of
  # textcolor, which is why it's defined here at all.
  'headtextcolor': '',

  # color of text in the footer, including links; defaults to the
  # value of textcolor
  'footertextcolor': '',

  # Custom CSS
  'cssfiles': ['_static/style.css'],

  # Custom JS
  'scriptfiles': ['_static/versions.js']
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NYAWCdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NYAWC.tex', 'N.Y.A.W.C Documentation',
     'Tijme Gommers', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nyawc', 'N.Y.A.W.C Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NYAWC', 'N.Y.A.W.C Documentation',
     author, 'NYAWC', 'A web crawler that gathers more than you can imagine.',
     'Miscellaneous'),
]

# Title of the documentation
html_title = "Not Your Average Web Crawler"

# Home button title
html_short_title = "Home"

# Sidebar contents
html_sidebars = {
  '**': ['sidebar.html', 'searchbox.html'],
}

# Absolute link the the source code
def linkcode_resolve(domain, info):
    if domain != 'py':
        return None

    if not info['module']:
        return None

    filename = info['module'].replace('.', '/')
    return "https://github.com/tijme/not-your-average-web-crawler/tree/{}/{}.py".format(semver, filename)

# Napoleon
napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc  = True

# Always make sure current release is in releases.json
import json

releases = json.loads(open('_static/releases.json').read());

releases[release] = True

with open('_static/releases.json', 'w') as outfile:
    json.dump(releases, outfile)