Redips
======

Redips is a Python based web crawler.
Compatible with Python 2.7.X

Redips can be used to generate:
- An index that maps every word Redips encounters with a set of URLs it finds the word on.
- A graph that maps every URL Redips encounters to a list of URLs on that page.

Index: {keyword1 : set([URL1, URL2,...]),
		keyword2 : set([URL3, URL4,...]),
		...}

Graph: {URL1 : [outlink1, outlink2,...],
		URL2 : [outlink3, outlink4,...],
		...}

To use:
```python
>>> from redips import Redips
>>> redips = Redips('http://github.com')
>>> redips.crawl()
```

The Redips constructor takes 2 arguments both of which are optional
```python
>>> from redips import Redips
>>> redips = Redips(seed_url='http://foo.bar', pickle='abc.pickle')
```

URLs can also be added to the list of URLs to be crawled as:
```python
>>> redips.add_url('http://google.com')
>>> redips.to_crawl
['http://google.com']
>>>
```

To save the state of a Redips object:
```python
>>> redips.save()
```

To load a previously pickled Redips object:
```python
>>> from redips import *
>>> redips = load('redips.pickle') # Or whichever pickle file your crawler is saved in
>>> redips.crawl() # Resume crawling from where it left
```

To specify a file other than the default redips.pickle file for pickling the crawler:
```python
>>> from redips import *
>>> redips = Redips(pickle='foo.pickle')
```

To crawl a single page:
```python
>>> redips.crawl_page('http://foo.bar')
```

To access the index:
```python
>>> redips.get_index()
```

To access the graph:
```python
>>> redips.get_graph()
```

To reset the list of URLs to crawl:
```python
>>> redips.reset_to_crawl()
```

To merge the index with another index:
```python
>>> redips.merge_index(index)
```

To merge the graph with another graph:
```python
>>> redips.merge_graph(graph)
```

To merge the data of another Redips object with your Redips object:
```python
>>> redips.merge(anotherRedips)
```
