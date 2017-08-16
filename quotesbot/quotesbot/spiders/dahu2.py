# -*- coding: utf-8 -*-
import scrapy

class Dahu2Spider(scrapy.Spider):
    name = 'dahu2'
    allowed_domains = ['www.sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_197495.html']

    def __init__(self,myurl=None,*args,**kwargs):
        super(Dahu2Spider,self).__init__(*args,**kwargs)
        if myurl==None:
            myurl=Dahu2Spider.start_urls[0]
        print("要爬取的网址为:%s"%myurl)
        self.start_urls=["%s"%myurl]

    def parse(self, response):
        yield {
            'title':response.xpath('//title/text()').extract_first()
        }
        print response.xpath('//title/text()').extract_first()
