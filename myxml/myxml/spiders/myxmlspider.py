# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1405603123.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        i['title']=node.xpath('//item/title/text()').extract()
        i['link']=node.xpath('//item/link/text()').extract()
        i['author']=node.xpath('//item/author/text()').extract()
        print len(i['title'])
        for j in range(len(i['title'])):
            print i['title'][j]
            print i['link'][j]
            print i['author'][j]
        return i
