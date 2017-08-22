#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.cnblogs.com/dahu-daqing/'),
        gevent.spawn(f, 'https://www.liaoxuefeng.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
])