#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
import urllib
import urllib2

url = 'https://www.zhihu.com/'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
values = {'username': '707133607@qq.com', 'password': 'XXXX'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()