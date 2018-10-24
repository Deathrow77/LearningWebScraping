import scrapy

class ArticleScraper(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        urls = [
             'http://en.wikipedia.org/wiki/Python_'
             '%28programming_language%29',
             'https://en.wikipedia.org/wiki/Functional_programming',
             'https://en.wikipedia.org/wiki/Monty_Python']
        return [scrapy.Request(url=url, )]
