#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 异常
#本来是要体验异常,应该报错4.3,但是我这边还是会返还read的内容,做成网页又打不开,好奇怪.
import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    response=urllib2.urlopen(req)
    print response.read()
    # print 'ok'
except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    print e.reason