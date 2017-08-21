#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 模拟浏览器,headers属性
import urllib2
url='http://blog.csdn.net/weiwei_pig/article/details/69891700'
user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
header = { 'User-Agent' : user_agent }
# data=
request = urllib2.Request(url, headers=header)
# request = urllib2.Request(url)
response= urllib2.urlopen(request)
with open('t3.url.html','w')as f:
    f.write(response.read())
print response.getcode()