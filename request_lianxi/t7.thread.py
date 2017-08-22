#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
# 多线程热身
import requests, lxml.html
import sys, os
import threading

reload(sys)
sys.setdefaultencoding('UTF-8')


class A(threading.Thread):
    def __init__(self):
        super(A, self).__init__()
        # threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print 'I am thread A'


class B(threading.Thread):
    def __init__(self):
        # threading.Thread.__init__(self)
        super(B, self).__init__()

    def run(self):
        for i in range(10):
            print 'I am thread B'
if __name__ == '__main__':
    t1=A()
    t1.start()
    t2=B()
    t2.start()
