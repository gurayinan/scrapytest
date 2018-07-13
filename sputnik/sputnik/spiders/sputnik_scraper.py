# -*- coding: utf-8 -*-
import scrapy


class SputnikScraperSpider(scrapy.Spider):
    name = 'sputnik-scraper'
    allowed_domains = ['tr.sputniknews.com']
    start_urls = ['http://tr.sputniknews.com/']

    def parse(self, response):
        for title in response.css('li.b-highlights__item'):
            yield {'title': title.css('a ::text').extract_first()}
