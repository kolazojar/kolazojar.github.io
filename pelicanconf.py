#!/usr/bin/env python

from datetime import date

# Basic settings.
AUTHOR = 'Matt Krol'
SITENAME = 'Matt Krol'
SITESUBTITLE = 'Electrical Engineer, Bassist, Composer'
SITEURL = ''
TIMEZONE = 'EST'
PATH = 'content'
DEFAULT_LANG = 'en'
THEME = 'theme'
DEFAULT_CATEGORY = 'Misc'
CURRENTYEAR = date.today().year

# Disable feeds for development.
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Menu settings.
DISPLAY_CATEGORIES_ON_MENU = None
DISPLAY_PAGES_ON_MENU = True

# Don't render this information.
ARTICLE_LANG_SAVE_AS = ''
PAGE_LANG_SAVE_AS = ''
DRAFT_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''
DRAFT_PAGE_LANG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# URL and SAVE settings.
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Use all templates except for authors.
DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives']

# Static paths for images, pdfs, etc.
STATIC_PATHS = ['images', 'docs']

# Markdown settings.
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
    },
    'output_format': 'html5',
}