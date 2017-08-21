#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
# 代理服务器的设置,好像用不起来,明天再研究一下
import urllib2

def use_proxy(proxy_adder, url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    header = {'User-Agent': user_agent}

    proxy = urllib2.ProxyHandler({'http': proxy_adder})
    # proxy = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    request = urllib2.Request(url)
    # request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request,timeout=20)
    return response.read()


if __name__ == '__main__':
    proxy_adder = 'http://218.75.101.66:3128'
    # "182.141.60.2:9000"
    url = 'https://www.baidu.com/s?wd=ip%E5%9C%B0%E5%9D%80&rsv_spt=1&rsv_iqid=0x8a8bc1d300003c8e&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=6&rsv_sug1=6&rsv_sug7=101'
    url='http://ip.chinaz.com/'
    data = use_proxy(proxy_adder, url)
    with open('t6.url.html', 'w')as f:
        f.write(data)
