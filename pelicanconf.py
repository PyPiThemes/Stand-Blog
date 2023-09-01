# Import required module
import os

# Author and site information
AUTHOR = 'Admin'
SITENAME = 'Stand Blog'
SITEURL = 'https://stand-blog-blog-pelican-theme.pages.dev'
CATEGORY = 'Blog'
SITEDESCRIPTION = 'My Blog'
DEFAULT_LOCALE = 'en_US'

# Contact information
CONTACT_INFORMATION = {
    'Phone Number': '090-484-8080',
    'Email Address': 'info@company.com',
    'Street Address': '123 Aenean id posuere dui, Praesent laoreet 10660'
}

# Content settings
PATH = 'content/'

# Time and language settings
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

# Appearance settings
SITELOGO = ""
FAVEICON = "favicon.png"
DELETE_OUTPUT_DIRECTORY = True
THEME = 'theme/'

# Feed generation settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Article settings
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

# Page settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Index settings
INDEX_URL = '/'
INDEX_SAVE_AS = 'index.html'

# Category settings
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_PAGINATION_URL = 'category/{slug}/page/{number}/'
CATEGORY_PAGINATION_SAVE_AS = 'category/{slug}/page/{number}/index.html'

# Tag settings
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_PAGINATION_URL = 'tag/{slug}/page/{number}/'
TAG_PAGINATION_SAVE_AS = 'tag/{slug}/page/{number}/index.html'

# Author settings
AUTHOR_URL = 'author/{slug}/'
AUTHOR_URL_SAVE_AS = 'author/{slug}/index.html'

# Pages
TEMPLATE_PAGES = {
    'contact.html': 'contact.html',
    '404.html': '404.html',
}

# Static files
STATIC_PATHS = ['extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Blogroll links
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    ('You can modify those links in your config file', '#'),
)

# Social media links
SOCIAL_MEDIA_LINKS = (
    ('Twitter', 'https://twitter.com/your_twitter_username'),
    ('Facebook', 'https://facebook.com/your_facebook_username'),
    ('GitHub', 'https://github.com/your_github_username'),
    ('Youtube', 'https://youtube.com/your_youtube_username'),
    ('Tiktok', ''),
    # Add more social media links here
)

# Pagination settings
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Plugins
PLUGINS_PATH = os.path.join(os.getcwd(), "pelican-plugins")
PLUGIN_PATHS = [PLUGINS_PATH]
PLUGINS = ["sitemap", "articlejson", "share_post"]

# Sitemap settings
SITEMAP = {
    'siteurl': SITEURL,
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily',
    },
    'exclude': [],  # ex: ['categories', 'tags']
}

# SEO settings
OPEN_GRAPH = True
TWITTER_TAGS = True
YOUR_TWITTER_HANDLE = "pytheme"
REL_CANONICAL = True
USE_GOOGLE_FONTS = True

# KwesForms settings
KWESFORMS_ACTION = "https://kwesforms.com/api/foreign/forms/S9CLmleGJB99fnH4f3kw"

# Disqus settings
DISQUS = True

# HIGHLIGHTER = True