#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
#
import re
ss='导航上海C级W'
for m in re.finditer('\w+',ss):
    ss= ss.replace(m.group(),m.group()+'\n')
    print ss
    print [i for i in ss.decode('utf-8')]