#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wojtek Cichon'
SITENAME = 'Six Million Ways to DIY'
SITESUBTITLE = "thoughts on software, DIY culture, anything really"
SITEURL = 'https://wojtekidd.org/6mlndiy'
PATH = 'content'
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SLUGIFY_SOURCE = 'title'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 3
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Blog'
DISPLAY_CATEGORIES_ON_MENU = True


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

STATIC_PATHS = ['images', 'pages']

# Specify name of a theme installed via the pelican-themes tool
THEME = "brutalist"
## used for OG tags and Twitter Card data on index page
# SITEIMAGE = 'site-cover.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Six Million Ways to DIY - thoughts on software, DIY culture, anything really'
## path to favicon
#FAVICON = 'pelly.png'
## path to logo for nav menu (optional)
LOGO = 'pelly.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = '6mlndiy'
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@wojtekidd'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = True
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
#MENUITEMS = [('Blog', '/blog')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
TWITTER = 'https://twitter.com/wojtekidd'
GITHUB = 'https://github.com/wojtekidd'
GOODREADS = 'https://www.goodreads.com/user/show/950927-wojtek'
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
#DISQUS_SITENAME = 'brutalistpelican'
## Gravatar
## Commenting mine out so you can see how the theme looks without one
## See https://mamcmanus.com to see what it looks like with a Gravatar
GRAVATAR = 'https://s.gravatar.com/avatar/f3365ae331876cd8553167f3354d06ba?s=256'

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins', '/Users/wojtek/6mlndiy/pelican-plugins']
PLUGINS = ['sitemap', 'category_order', 'gzip_cache']

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}
