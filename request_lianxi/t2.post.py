#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text

#传json格式数据
import json
url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text