# -*- coding: utf-8 -*-
import scrapy

#通过下一篇来爬取
class CommonSpiderSpider(scrapy.Spider):
    name = 'common_spider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/blog_53c7cd330102x2pq.html']

    def parse(self, response):
        print response.xpath('//title/text()').extract_first()
        print response.xpath('//div[@class="articalfrontback SG_j_linedot1 clearfix"]//span/text()').extract_first()
        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        next_page_url = response.xpath('//div[@class="articalfrontback SG_j_linedot1 clearfix"]//a/@href').extract_first()
        if next_page_url is not None:
            # print response.urljoin(next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))
