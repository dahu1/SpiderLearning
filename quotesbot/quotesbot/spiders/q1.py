#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
import scrapy
from lxml import etree

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"][last]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

            next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))
    def parse2(self,response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    def parse3(self,response):
        root = etree.HTML(response.body)
        self.log('hehe')
        for i in root:
            print i.text,i.tag
        self.log('Saved file %s' % len(root))
