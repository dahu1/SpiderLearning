# -*- coding: utf-8 -*-
import scrapy
import urllib2
#没有写完,报错 http://image.baidu.com/robots.txt 里不让爬,需要加user-agent,还不会加
class BaiduPicSpider(scrapy.Spider):
    name = 'baidu_pic'
    # start_urls = ['http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0']
    index = 1

    def start_requests(self):
        urls = ['http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0']

        url = 'http://www.server.com/login'
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
        values = {'username': 'cqc', 'password': 'XXXX'}
        headers = {'User-Agent': user_agent}
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data, headers)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,headers='Baiduspider')


    def parse(self, response):
        for i in response.xpath('//img[@class="main_img img-hover"]/../@href'):
            print i.extract()
            # yield {'title': i.extract()}
        self.index += 1
        # a = response.xpath(
        #     '//div[@class="thread_list_bottom clearfix"]//a[@class="next pagination-item "]/text()').extract_first()
        # if a != None:
        #     print '>>>\n', a, "第%s页" % self.index, '\n>>>'
        #     yield {'glap': '>>>' + a + "this is %s page" % self.index}
        #     #
        #     next_page_url = response.xpath(
        #         '//div[@class="thread_list_bottom clearfix"]//a[@class="next pagination-item "]/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))