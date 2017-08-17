# -*- coding: utf-8 -*-
import scrapy


class KindleTiebaSpider(scrapy.Spider):
    name = 'kindle_tieba'
    start_urls = ['http://tieba.baidu.com/f?kw=kindle&ie=utf-8&pn=0']
    index = 1

    def parse(self, response):
        for i in response.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@title'):
            print i.extract()
            yield {'title': i.extract()}
        self.index += 1
        a = response.xpath(
            '//div[@class="thread_list_bottom clearfix"]//a[@class="next pagination-item "]/text()').extract_first()
        if a != None:
            print '>>>\n', a, "第%s页" % self.index, '\n>>>'
            yield {'glap': '>>>' + a + "this is %s page" % self.index}
            #
            next_page_url = response.xpath(
                '//div[@class="thread_list_bottom clearfix"]//a[@class="next pagination-item "]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))