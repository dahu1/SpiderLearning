#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
#
import sys
import lxml.html as H
reload(sys)
sys.setdefaultencoding( "utf-8" )

with open("quotes-1.html",'r')as f:
    a=H.document_fromstring(f.read().decode("utf-8"))

for i in  a.xpath('//div[@class="quote"]/span[@class="text"]/text()'):
    print i
print a.xpath('//li[@class="next"]/a/@href')
# print H.tostring(a)