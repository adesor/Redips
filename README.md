Redips
======

Redips is a Python based web crawler.

To use:
In Python 2.7.X,

>>> from redips import Redips
>>> redips = Redips()
>>> redips.crawl('http://github.com')


To fetch only the links on the seed url:

>> redips.extract_links('http://github.com')

