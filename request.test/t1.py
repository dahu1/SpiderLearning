#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
# 
import requests
r = requests.get('https://github.com/timeline.json')
r = requests.post('https://github.com/timeline.json')
print r.text
print r.encoding
