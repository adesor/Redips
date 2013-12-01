"""
Redips - A basic web crawler
Compatible with Python 2.7.X
"""
import urllib2
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urlparse import *

class Redips:
    """
    Redips is the crawler that crawls a seed url
    """
    def __init__(self):
        self.fetched_links = []
        self.crawled_links = []
        

    def crawl(self, seed_url):
        """
        crawl the input url for links
        string -> list(string)
        """
        
        print "Crawling " + seed_url

        # Extract links
        links_on_page = self.extract_links(seed_url)
        
        # Add the extracted links to the list of fetched links
        self.fetched_links.extend(links_on_page)
        
        # Add the seed url to the list of crawled links
        self.crawled_links.append(seed_url)

        # Recursively crawl fetched links
        for link in self.fetched_links:
            if link not in self.crawled_links:
                self.crawl(link)

        return self.fetched_links
            
    def get_url(self, url):
        """
        string -> Url
        Open the input url
        """
        try:
            url_object = urlopen(url)
        except urllib2.URLError:
            print "Invalid seed url"
            return
        
        # Redirect the url if possible
        redirected_url = url_object.geturl()
        redirected_url_object = urlopen(redirected_url)

        return redirected_url_object

    def get_source_page(self, url):
        """
        Url -> string
        Return the source page of the input url
        """
        return url.read()

    def extract_links(self, seed_url):
        """
        string -> list(string)
        Return a list of links on the input seed url
        """
        fetched_links = []
        url = None
        source_page = None

        # Open the seed url
        url = self.get_url(seed_url)
        
        # Get the source page of the url
        if url:
            source_page = self.get_source_page(url)
        
        if source_page:
            # Make a Beautiful Soup of the source page
            soup = BeautifulSoup(source_page)
        
            # Extract links
            for link in soup.find_all('a'):
                fetched_link = link.get('href')
                if fetched_link:
                    fetched_link = self.convert_to_absolute(url.geturl(), fetched_link)
                    fetched_links.append(fetched_link)

        return fetched_links

    def convert_to_absolute(self, seed_url, url):
        """
        string, string -> string
        Convert the input url from relative to absolute
        """
        parsed_link = urlparse(url)
            
        if not parsed_link.scheme:
            return urljoin(seed_url, url)
        else:
            return url
            
            
