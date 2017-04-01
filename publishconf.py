#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shengyi Qian'
SITENAME = 'Shengyi Qian'
SITEURL = 'https://jasonqsy.github.io'
TIMEZONE = 'Asia/Shanghai'

PATH = 'content'

DEFAULT_LANG = 'en'

THEME = "themes/pelican-elegant"

SITE_DESCRIPTION = "I'm a undergraduate student in the University of Michigan \
and major in Computer Science."

# Plugins
PLUGIN_PATHS = ["plugins"]

PLUGINS = ["render_math"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'mailto:jasonsyqian@gmail.com'),
          ('github', 'https://github.com/JasonQSY'),
          ('linkedin', 'https://linkedin.com/in/jasonqsy'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = 'UA-73612193-1'
DISQUS_SITENAME = "jasonqian"
GITHUB_URL = 'https://github.com/JasonQSY'
