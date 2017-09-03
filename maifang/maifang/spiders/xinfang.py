# -*- coding: utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
#新房


class XinfangSpider(scrapy.Spider):
    name = 'xinfang'
    # allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://newhouse.qd.fang.com/house/s/huangdao/']

    index = 1

    def parse(self, response):
        # with open('record.txt', 'a')as f:
        for i in response.xpath('//div[@class="clearfix"]'):
            print i.xpath('.//div[@class="nlcd_name"]/a/text()').extract_first().strip()
            print "address >>>",i.xpath('.//div[@class="address"]/a/@title').extract_first()
            # # yield {'title':i.extract()}
            # print 'area >>>',i.xpath('.//div[@class="area alignR"]/p/text()').extract_first()
            # print '总价 >>>',i.xpath('.//span[@class="price"]/text()').extract_first()+i.xpath('//span[@class="YaHei ml5"]/text()').extract_first()
            print '单价 >>>',''.join(i.xpath('.//div[@class="nhouse_price"]/*/text()').extract())
            # print
            # a = i.xpath('./p[@class="title"]/a/@title').extract_first()
            # b = "address >>> " + i.xpath('.//span[@class="iconAdress ml10 gray9"]/text()').extract_first()
            # # yield {'title':i.extract()}
            # c = 'area >>> ' + i.xpath('.//div[@class="area alignR"]/p/text()').extract_first()
            # d = '总价 >>> ' + i.xpath('.//span[@class="price"]/text()').extract_first() + i.xpath(
            #     '//span[@class="YaHei ml5"]/text()').extract_first()
            # e = '单价 >>> ' + i.xpath('.//p[@class="danjia alignR mt5"]/text()').extract_first()
            # f.write('%s\r\n%s\r\n%s\r\n%s\r\n%s\r\n\r\n' % (a, b, c, d, e))
        self.index += 1
        a = response.xpath('//a[@class="next"]/text()').extract_first()
        if a:
            print '>>>\n', a, "第%s页" % self.index, '\n>>>'
            b = '>>>\n' + a + "第%s页" % self.index + '\n>>>'
            # f.write(b)
            yield {'glap': '>>>' + a + "this is %s page" % self.index}

        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page_url != None:
            yield scrapy.Request(response.urljoin(next_page_url))
