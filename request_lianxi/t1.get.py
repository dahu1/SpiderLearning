#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 基本get请求

import requests
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

r = requests.get("https://www.baidu.com/")
r.encoding='utf-8'
print type(r)
print r.status_code
print r.encoding
#print r.text
print r.cookies
with open('t1.url.html','w')as f:
    f.write(r.text)

##加参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print r.url
