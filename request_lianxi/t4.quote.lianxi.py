#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 爬取网页,保存至html文件,然后在对其处理
import requests,lxml.html
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
r = requests.get("http://quotes.toscrape.com/")
r.encoding='utf-8'
with open('t4.url.html','w')as f:
    f.write(r.text)
with open("t4.url.html",'r')as f:
    # a=lxml.html.document_fromstring(f.read().decode("utf-8"))
    a=lxml.html.document_fromstring(f.read())

for i in  a.xpath('//div[@class="quote"]/span[@class="text"]/text()'):
    print i