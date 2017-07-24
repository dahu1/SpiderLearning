#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 用Request来访问网页
import urllib2

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
the_page= response.read()
with open('a.html','w') as f:
    f.write(the_page)