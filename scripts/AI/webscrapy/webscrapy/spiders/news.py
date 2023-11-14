import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['cbsnews.com']
    start_urls = ['http://cbsnews.com/']

    def parse(self, response):
        pass
