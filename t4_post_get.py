#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# POST和GET数据传送


import urllib
import urllib2

values = {"username": "1016903103@qq.com", "password": "XXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()