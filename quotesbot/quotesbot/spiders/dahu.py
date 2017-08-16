# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuotesbotItem
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class DahuSpider(scrapy.Spider):
    name = 'dahu'
    allowed_domains = ['sina.com.cn']
    start_urls = [
        'http://slide.news.sina.com.cn/s/slide_1_2841_197495.html',
        'http://slide.mil.news.sina.com.cn/k/slide_8_193_55924.html/d/1#p=1',
    ]
    def __init__(self,myurl=None,*args,**kwargs):
        super(DahuSpider,self).__init__(*args,**kwargs)
        if myurl==None:
            myurl=DahuSpider.start_urls[0]
        print("要爬取的网址为:%s"%myurl)
        self.start_urls=["%s"%myurl]

    def parse(self, response):
        item=QuotesbotItem()
        item['urlname']=response.xpath('//title/text()')
        print 'haha',item['urlname']
        print response.xpath('//title/text()').extract_first()
        pass
