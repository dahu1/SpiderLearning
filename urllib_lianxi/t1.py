#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# #直接爬取一个网页的代码,非常简单
import urllib2
response=urllib2.urlopen('http://quotes.toscrape.com/')
# request=urllib2.Request('http://quotes.toscrape.com/')  #注意,和上面的效果是一样的
# response=urllib2.urlopen(request)
with open('t1.url.html','w')as f:
    f.write(response.read())  #read的用法和文件的用法一样的

# ##获取一些信息参数
# print fi.info()         #返回与当前环境有关的信息
# print fi.getcode()      #爬取网页的状态码
# print fi.geturl()       #当前爬取的url地址

# print urllib2.quote('http://www.sina.com.cn')   #编码,放中文字符等等..
# print urllib2.unquote('http%3A//www.sina.com.cn')   #解码