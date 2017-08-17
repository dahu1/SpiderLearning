# -*- coding: utf-8 -*-
import scrapy

class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    # allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E9%9B%B6%E5%BA%A6%E5%90%9B%E4%B8%8A&ie=utf-8&tp=0']
    index=1
    def parse(self, response):
        for i in response.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@title'):
            print i.extract()
            yield {'title':i.extract()}
        self.index+=1
        a=response.xpath('//div[@class="thread_list_bottom clearfix"]//a[@class="next pagination-item "]/text()').extract_first()
        if a!=None:
            print '>>>\n',a,"第%s页"%self.index,'\n>>>'
            yield {'glap':'>>>'+a+"this is %s page"%self.index}
        #
            next_page_url = response.xpath('//div[@class="thread_list_bottom clearfix"]//a[@class="next pagination-item "]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
