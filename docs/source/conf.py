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
import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))


 
# https://stackoverflow.com/questions/56932004/how-to-document-options-in-an-ini-file-with-sphinx
# from sphinx.application import Sphinx
# from sphinx.util.docfields import Field

# def setup(app: Sphinx):
#     """Δημιουργία αντικειμένου texconfval (TeX Configuration Value).

#     Χρησιμοποιούμε τη μέθοδο
#     add_object_type(
#         directivename,
#         rolename,
#         indextemplate='',
#         parse_node=None,
#         ref_nodeclass=None,
#         objname='',
#         doc_field_types=[])

#     της Sphinx (δες ) με την οποία δημιουργούμε μία νέα οδηγία
#     ``.. texconfval::`` και ένα νέο ρόλο με το ίδιο όνομα
#     ``:texconfval:``
    
#     Parameters
#     ----------

#     texconfval : str
#         Η νέα οδηγία για την τεκμηρίωση ορισμάτων μίας εντολής των
#         LaTeX / TeX. Δημιουργεί παράλληλα και μία καταχώριση στο
#         index μέσω του parameter `indextemplate` (δες στη συνέχεια). 

#     texconfval : str
#         Ο νέος ρόλος για ενδοαναφορά στην περιγραφή των ορισμάτων
#         (που δημιουργούμε με την παραπάνω οδηγία).

#     objname : str
#         Η ονομασία της οδηγίας και του ρόλου (σαν αντικείμενα
#         της Python). Αν δε δοθεί, από προεπιλογή παίρνει τιμή
#         `texconfval`.

#     indextemplate : str
#         Η μορφή που θα έχει η καταχώριση στο index. Θα καταχωρείται
#         μαζί με (pair) τη φράση 'όρισμα εντολής'.

#     doc_field_types : list
#         Λίστα με τα πεδία που μπορούν να συνοδεύουν μία οδηγία
#         `texconfval`. Ορίζουμε τρία πεδία


#     Raises:
#        AttributeError, KeyError

#     """
#     app.add_object_type(
#         'texconfval',
#         'texconfval',
#         objname='tex configuration value',
#         indextemplate='pair: %s; όρισμα εντολής',
#         doc_field_types=[
#             Field('type', label='Type', has_arg=False, names=('type',)),
#             Field('default', label='Default', has_arg=False, names=('default',)),
#         ]
#     )


# -- Project information -----------------------------------------------------

project = 'Athena Docs'
copyright = '2020, Alex'
author = 'Alex'

# The full version, including alpha/beta/rc tags
release = '0.0.1'



# GENERAL CONFIGURATION

# 1. LOAD EXTENSIONS
#
# Add any Sphinx extension module names here, as strings. They
# can be extensions coming with Sphinx (named 'sphinx.ext.*') or
# your custom ones.

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
  #  "sphinxcontrib.programoutput",
    "sphinx.ext.imgconverter",
  #  'sphinxcontrib.inlinesyntaxhighlight',
    'sphinx.ext.napoleon',
]

# 1.1 Extensions Configuration

# -------------  ext.extlinks  -----------------------------------
# Aυτή τη ρύθμιση τη βρήκα στο
# https://github.com/sphinx-doc/sphinx/blob/3.x/doc/conf.py
# από το ίδιο το sphinx

extlinks = {
'duref': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'restructuredtext.html#%s', ''),
 
'durole': ('http://docutils.sourceforge.net/docs/ref/rst/'
                       'roles.html#%s', ''),
 
'dudir': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'directives.html#%s', ''),
 
'wiki': ('https://en.wikipedia.org/wiki/%s', ''),
 
'pywiki': ('https://wiki.python.org/moin/%s', ''),
 
'pyorg': ('https://docs.python.org/3/%s', ''),

'texinfo': ('http://tug.org/texinfohtml/latex2e.html#%s', ''),

'texpkg': ('https://ctan.org/pkg/%s', ''),

'wikibooks': ('https://en.wikibooks.org/wiki/LaTeX/%s', ''),
            }


# -------------  ext.todo  -----------------------------------

todo_include_todos = True
# -------------------------------------------------------------



# 2. DECLARE PATHS
#
# 2.1 Templates
#
# Add any paths that contain templates here, relative to this
# directory.

templates_path = ['_templates']


# 2.2 Static Content
#
# Add any paths that contain custom static files (such as style
# sheets) here, relative to this directory. They are copied after
# the builtin static files, so a file named "default.css" will
# overwrite the builtin "default.css".
html_logo = '_static/athena.png'
html_static_path = ['_static']

html_context = {
    'css_files': [
        
        # override wide tables in RTD theme
        '_static/css/theme_overrides.css',
        
     
        ],
     }

# def setup(app):
#         app.add_stylesheet('_static/css/custom.css') 

# 3. MASTER DOCUMENT CONFIG

"""
The language for content autogenerated by Sphinx.

Refer to documentation for a list of supported languages. This is
also used if you do content translation via gettext catalogs. 
Usually you set "language" from the command line for these cases.
"""

language = 'el'

#-----------------

"""
Pygment style
"""

pygments_style = 'sphinx'

#------------------

"""
Tells the project the name of the home page.
"""

master_doc = 'index'

#----------------

"""
Numbering figures an tables allover the document.
"""

numfig = True

numfig_format = {
    'figure': 'Εικ. %s',
    'table': 'Πιν. %s',
    'code-block': 'Κωδ. %s',
    'section': 'Ενότητα. %s',
    }

#----------------------

"""
A string of reStructuredText that will be included at the
beginning of every source file that is read (συντομεύσεις).
"""

rst_prolog = """
.. |latex| replace:: LaTeX
.. |tex| replace:: TeX
.. |euro|    unicode:: U+20AC .. EURO
.. |laquos|  unicode:: U+2039 .. SINGLE LEFT-POINTING ANGLE QUOTATION MARK
.. |raquos|  unicode:: U+203A .. SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
.. |lanbr|   unicode:: U+3008 .. LEFT ANGLE BRACKET
.. |ranbr|   unicode:: U+3009 .. RIGHT ANGLE BRACKET
.. |trade|  unicode:: U+02122 .. TRADE MARK SIGN
.. |times|  unicode:: U+000D7 .. MULTIPLICATION SIGN
.. |pound|  unicode:: U+000A3 .. POUND SIGN
.. |sect|   unicode:: U+000A7 .. SECTION SIGN
.. |rarr|   unicode:: U+02192 .. RIGHTWARDS ARROW
.. |reg|    unicode:: U+000AE .. REGISTERED SIGN
.. |rdquo|  unicode:: U+0201D .. RIGHT DOUBLE QUOTATION MARK
.. |ldquo|  unicode:: U+0201C .. LEFT DOUBLE QUOTATION MARK
.. |para|   unicode:: U+000B6 .. PILCROW SIGN
.. |lt|     unicode:: U+0003C .. LESS-THAN SIGN
.. |larr|   unicode:: U+02190 .. LEFTWARDS ARROW
.. |gt|     unicode:: U+0003E .. GREATER-THAN SIGN
.. |dollar| unicode:: U+00024 .. DOLLAR SIGN
.. |middot| unicode:: U+000B7 .. MIDDLE DOT
.. |rsquo|  unicode:: U+02019 .. RIGHT SINGLE QUOTATION MARK
.. |lsquo|  unicode:: U+02018 .. LEFT SINGLE QUOTATION MARK
.. |hellip| unicode:: U+02026 .. HORIZONTAL ELLIPSIS
.. |Dagger| unicode:: U+02021 .. DOUBLE DAGGER
.. |dagger| unicode:: U+02020 .. DAGGER
.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN
.. |lowbar| unicode:: U+0005F .. LOW LINE
.. |verbar| unicode:: U+0007C .. VERTICAL LINE
.. |raquo|  unicode:: U+000BB .. RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
.. |laquo|  unicode:: U+000AB .. LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
.. |sol|    unicode:: U+0002F .. SOLIDUS
.. |vspace|  unicode:: U+2423 .. VISIBLE SPACE
.. |stigmas|  unicode:: U+03DA .. GREEK SMALL STIGMA
.. |stigmac|  unicode:: U+03DA .. GREEK CAPITAL STIGMA
.. |dash|   unicode:: U+02010 .. HYPHEN
.. |ndash|  unicode:: U+02013 .. EN DASH
.. |mdash|  unicode:: U+02014 .. EM DASH

"""

#----------------- 

# 4. HTML OUTPUT CONFIG
#
# 4.1 HTML Theme
# The theme to use for HTML and HTML Help pages. See the
# documentation for a list of builtin themes.

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    # prev_next_buttons_location': Location to display Next and Previous buttons. This can be either bottom, top, both , or None. Default: 'bottom',
    'prev_next_buttons_location': 'both',
    # style_external_links': Add an icon next to external links. Default: False,
    'style_external_links': False,
    # style_nav_header_background': Changes the background of the search area in the navigation bar. The value can be anything valid in a CSS background property. Default: 'white',
    #'style_nav_header_background': 'white',
    # Toc options
    # collapse_navigation: With this enabled, navigation entries are not expandable – the [+] icons next to each entry are removed. Default: True
    'collapse_navigation': True,
    # sticky_navigation: Scroll the navigation with the main page content as you scroll the page. Default: True
    'sticky_navigation': True,
    # navigation_depth: The maximum depth of the table of contents tree. Set this to -1 to allow unlimited depth. Default: 4
    'navigation_depth': 5,
    # includehidden:Specifies if the navigation includes hidden table(s) of contents – that is, any toctree directive that is marked with the :hidden: option. Default: True,
    #'includehidden': True,
    # titles_only: When enabled, page subheadings are not included in the navigation. Default: False
    #'titles_only': False,
    # style_external_links': Add an icon next to external links. Default: False,
    'style_external_links': True,
}

# 4.2 HTML Various
#
# 4.2.1 Compact lists

html_compact_lists = True

# 4.2.2 Exclutions
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = []


# 5. LATEX OUTPUT CONFIG
#
# 5.1       .tex file output

latex_engine = 'xelatex'

latex_show_urls = 'no' # εναλλακτικά 'footnote', 'inline'

#latex_toplevel_sectioning = 'part'

latex_show_pagerefs = True

latex_additional_files = ['mystyle.tex.txt']


latex_elements = {
    
    'preamble': r'\input{mystyle.tex.txt}',

 #   'maketitle': r'\\sphinxmaketitle',
    
    'fontpkg': r'''
\setmainfont{Lato}
\setsansfont{DejaVu Sans}
\setmonofont{Consolas}
''',
    
    'papersize': 'a4paper',
    
    'tableofcontents': '\\dominitoc\\sphinxtableofcontents',
    
    'fncychap': r'\usepackage[Sonny]{fncychap}',
    # εναλλακτικά: Bjornstrup, Bjornstrup, Lenny, Glenn, Conny,
    # Renje, Sonny

    'printindex': r'\footnotesize\raggedright\printindex',

    'sphinxsetup': 'verbatimwithframe=false',

    
}



# 5.2       .pdf file output

latex_documents = [
  ('latex/index', 'LatexGuide.tex', f'Latex Guide', u'Alex', 'manual'),
  ('rest/index', 'RestGuide.tex', f'RestructuredText Guide', u'Alex', 'manual'),
]


