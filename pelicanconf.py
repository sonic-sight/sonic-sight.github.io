#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# TODO: comment out this in production, possibly remove it from
# publishconf.py
LOAD_CONTENT_CACHE = False

AUTHOR = 'AUTHOR'
SITENAME = 'sonic-sight'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = [ 'examples', 'images', ]
GITHUB_ICON = 'images/github-32px.png'
GITHUB_PATH = 'https://github.com/sonic-sight'
OUTPUT_PATH = 'output'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

THEME = './theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


### TODO: maybe improve the videos a bit, possibly add poster image and
### different video formats and resolutions
### ```
### <video src="examples/video3.webm" width="320" height="200" controls preload></video>
### 
### <video poster="poster.jpg" width="618" height="347" controls preload> 
###     <source src="video.mp4" media="only screen and (min-device-width: 568px)"></source> 
###     <source src="video.iphone.mp4" media="only screen and (max-device-width: 568px)"></source> 
###     <source src="video.webm"></source> 
### </video>
### ```
