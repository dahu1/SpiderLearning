#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
import urllib
import urllib2
url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'

values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
with open('a.html','w') as f:
    f.write(the_page)