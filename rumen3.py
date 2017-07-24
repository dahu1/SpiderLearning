#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 异常
import urllib2

request = urllib2.Request('http://www.xxxxx.com')
# urllib2.urlopen(request)
try:
    urllib2.urlopen(request)
    print 'ok'
except urllib2.URLError, e:
    print e.reason      #没有出现错误,还真的有这个鸟网站...

