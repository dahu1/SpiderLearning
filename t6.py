#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
#
import re
a='I miss "\you5" '
print a
print re.search(r'\\',a).group()
print re.search(r'"',a).group()
print re.search('"',a).group()
