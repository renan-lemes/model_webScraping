import scrapy
from scrapy.crawler import CrawlerProcess


class SpiderActions(scrapy.Spider):
    name = 'spider_actions'

    def start_requests(self):
        urls = ['href1', 'href2']
        for url in urls:
            yield url

    def parse(self, response):
        html_file = 'dc_actions.html'
        with open(html_file, 'wb') as fout:
            fout.write(response.body)

    def parse2(self, response):
        pass
