#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 爬取网页,不保存html文件呢
import requests,lxml.html
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
r = requests.get("http://quotes.toscrape.com/")
r.encoding='utf-8'

a=lxml.html.document_fromstring(r.text)

for i in  a.xpath('//div[@class="quote"]/span[@class="text"]/text()'):
    print i