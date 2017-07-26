#!/usr/bin/python
#coding=utf-8
#author=dahu
# tou 57
# yao 70
# xiong 88
# tun 89
#jiankuan 38  wei 90
import urllib
import urllib2

page = 1
url = 'https://list.tmall.com/search_product.htm?spm=a221t.1476805.2109261262.13.242ff89cPUewEe&cat=50025265&active=1&style=g&from=sn_1_rightnav&acm=lb-zebra-7419-257471.1003.4.405205&sort=new&search_condition=71&shopType=any&tmhkmain=0&scm=1003.4.lb-zebra-7419-257471.OTHER_14403889607042_405205&industryCatId=50025265#J_Filter'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    with open('a.html','w')as f:
        f.write(response.read())
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
