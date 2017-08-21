#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 设置超时时间,时间超了会引发异常
import urllib2
for i in range(10):
    try:
        # url = 'http://blog.csdn.net/weiwei_pig/article/details/69891700'
        url='https://www.baidu.com/'
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request,timeout=0.01)
        print(len(response.read()))
    except Exception as e:
        print "ERROR!"+str(e)
