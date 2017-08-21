#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
#客户端和服务器之间的消息传递,使用http协议
#共6种
import urllib2

#get
request=urllib2.Request('http://quotes.toscrape.com/')  #注意,和上面的效果是一样的
response=urllib2.urlopen(request)
with open('t1.url.html','w')as f:
    f.write(response.read())
