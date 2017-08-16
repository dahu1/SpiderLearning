#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
from scrapy import Spider
class FirstSpider(Spider):
    name='first'
    allowed_domains=["baidu.com"]
    start_urls=['http://www.baidu.com']
    def parse(self, response):
        pass