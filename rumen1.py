#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
#

import urllib
import urllib2

url = 'https://www.baidu.com'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
values = {'username': 'cqc', 'password': 'XXXX'}
header = {'User-Agent': user_agent}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)', 'Referer': 'http://www.zhihu.com/articles'} #反盗链,对付防盗链，服务器会识别headers中的referer是不是它自己

# data = urllib.urlencode(values)
request = urllib2.Request(url,  headers=header)
response = urllib2.urlopen(request)
page = response.read()
with open('a.html','w') as f:
    f.write(page)
print response
