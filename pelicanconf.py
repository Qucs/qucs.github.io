#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Qucs Team'
SITENAME = u'Qucs project: Quite Universal Circuit Simulator'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

#DELETE_OUTPUT_DIRECTORY = True

THEME = 'theme'
CSS_FILE = 'qucsweb.css'

# see https://github.com/getpelican/pelican/issues/1065
# keep news/blog in its own directory
ARTICLE_PATHS = ('news',)
ARTICLE_URL = 'news/{slug}.html'
ARTICLE_SAVE_AS = 'news/{slug}.html'

PAGE_PATHS = ('pages',)
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = 'news/category/{slug}.html'
CATEGORY_URL = 'news/category/{slug}.html'
TAG_SAVE_AS = 'news/tag/{slug}.html'
TAG_URL = 'news/tag/{slug}.html'
DIRECT_TEMPLATES = ('index', 'news_index')
PAGINATED_DIRECT_TEMPLATES = ('news_index', )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'docs', 'examples', 'tech', 'qucs-tab.ico']
EXTRA_PATH_METADATA = {
    'qucs-tab.ico': {'path': 'qucs-tab.ico'},
    }
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
