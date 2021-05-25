#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Komeil Parseh'
SITENAME = 'Komeil Parseh'
SITEURL = ''

GOOGLE_ANALYTICS = 'bnZpuUMrdM-_RFKk-SGTLCMLJXR8wh27Ui4DRVovSlM'
PATH = 'content'
STATIC_PATHS = [
    'images',
    'extra',  # this
]
TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme Setting
THEME = 'blue-penguin'
# all the following settings are *optional*

# HTML metadata
SITEDESCRIPTION = 'A blog for writing anything related to technology'

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME = True
DISPLAY_MENU = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
# Generate links to categories and tags following the same structure but without the .html extension

CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAG_URL = 'tags/{slug}/'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS ='archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# additional menu items
MENUITEMS = (
    ('GitHub', 'https://github.com/komeilparseh'),
    ('Persian Blog', 'https://virgool.io/@parseh'),
)

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/sitemap.xml':{'path':'sitemap.xml'}
}
