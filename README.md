Redips
======

Redips is a Python based web crawler.
Compatible with Python 2.7.X

To use:
```python
>>> from redips import Redips
>>> redips = Redips()
>>> redips.crawl('http://github.com')
```

To fetch only the links on the seed url:
```python
>>> redips.extract_links('http://github.com')
```
