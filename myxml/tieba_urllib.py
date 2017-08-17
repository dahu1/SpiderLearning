#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
#这个本来打算不用scrapy库,用urllib写,还没弄玩,发现还是框架方便一些
import urllib
import urllib2

url = 'https://tieba.baidu.com/f?kw=%E9%9B%B6%E5%BA%A6%E5%90%9B%E4%B8%8A&fr=index&fp=0&ie=utf-8'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.read()
    print response.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason