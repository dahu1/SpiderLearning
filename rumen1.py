#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
#

import urllib
import urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
values = {'username': 'cqc', 'password': 'XXXX'}
headers = {'User-Agent': user_agent}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)', 'Referer': 'http://www.zhihu.com/articles'} #反盗链,对付防盗链，服务器会识别headers中的referer是不是它自己

data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

print response
