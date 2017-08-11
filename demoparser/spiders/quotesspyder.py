# -*- coding: utf-8 -*-
import scrapy


class QuotesspyderSpider(scrapy.Spider):
    name = "quotesspyder"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
