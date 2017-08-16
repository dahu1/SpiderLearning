# -*- coding: utf-8 -*-
import scrapy

#通过目录来爬
class CommonSpider2Spider(scrapy.Spider):
    name = 'common_spider2'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1405603123_0_1.html']

    def parse(self, response):
        for i in response.xpath('//div[@class="articleList"]//span[@class="atc_title"]/a/text()'):
            print i.extract()
            yield {'text':i.extract()}
        print '>>>\n',response.xpath('//div[@class="SG_page"]//li[@class="SG_pgnext"]/a/@title').extract_first(),'\n>>>'
        yield {'glap':response.xpath('//div[@class="SG_page"]//li[@class="SG_pgnext"]/a/@title').extract_first()}

        next_page_url = response.xpath('//div[@class="SG_page"]//li[@class="SG_pgnext"]/a/@href').extract_first()
        if next_page_url is not None:
            print response.urljoin(next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))


