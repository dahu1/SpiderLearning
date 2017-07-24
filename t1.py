#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 普通打开网页
import urllib2
keywd='hello'
url='https://www.baidu.com/s?wd='+keywd
response = urllib2.urlopen('http://python.org/')
# req = urllib2.Request('https://www.baidu.com/')
# response = urllib2.urlopen(req)
html = response.read()
with open('a.html','w') as f:
    f.write(html)