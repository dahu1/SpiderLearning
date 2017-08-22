#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 使用代理
import requests
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
proxies = {
  # "http": "http://113.140.43.136:80",
"http": "http://111.155.116.196:8123",
}
# r = requests.get("http://httpbin.org/ip", proxies=proxies)
r = requests.get("http://ip.chinaz.com/",proxies=proxies)
# print r.text
with open('t3.url.html','w')as f:
    f.write(r.text)