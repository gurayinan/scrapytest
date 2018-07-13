import scrapy


class SputnikSpider(scrapy.Spider):
    name = 'sputnik-spider'
    start_urls = ['https://tr.sputniknews.com/']

    def parse(self, response):
        for title in response.css('li.b-highlights__item'):
            yield {'title': title.css('a ::text').extract_first()}

