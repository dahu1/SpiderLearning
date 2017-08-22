#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 按下一页,爬取全部网页,感觉普通的太慢了,还是框架爬的快
import requests,lxml.html
import sys,os
reload(sys)
sys.setdefaultencoding('UTF-8')

def htmlpage_down(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    a=lxml.html.document_fromstring(r.text)
    return a

if __name__ == '__main__':
    ##知道网页的规律
    # for i in range(1,11):
    #     print 'Index %s page'%i
    #     a=htmlpage_down("http://quotes.toscrape.com/"+'page/%s/'%i)
    #     for j in a.xpath('//div[@class="quote"]/span[@class="text"]/text()'):
    #         print j
    ##不知道规律,通过下一页来寻找
    url="http://quotes.toscrape.com/"
    a = htmlpage_down(url)
    for j in a.xpath('//div[@class="quote"]/span[@class="text"]/text()'):
        print j
    next_page_url=a.xpath('//li[@class="next"]/a/@href')[0]
    print next_page_url
    while next_page_url!='':
        a = htmlpage_down(url+next_page_url)
        for j in a.xpath('//div[@class="quote"]/span[@class="text"]/text()'):
            print j
        if a.xpath('//li[@class="next"]/a/@href'):
            next_page_url=a.xpath('//li[@class="next"]/a/@href')[0]
        else:
            next_page_url=''
        print next_page_url


