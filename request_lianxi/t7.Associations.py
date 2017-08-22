#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
#多线程更改变量
import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(0.5)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)       #给生成器里传参,同时获取生成器里的值
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

def gg():
    n=''
    # for i in range(5):
    i=0
    while True:
        n=yield i   #通过send传入到n
        if not n:
            pass
        else:
            print 'hehe',n
            i=100   #传进参数n的时候,使得i的值也变化了
        i+=1

if __name__=='__main__':
    c = consumer()
    produce(c)
#     a=gg()
#     print a.send(None)
#     print a.next()
#     print a.send(None)
#     print a.send(9)
#     print a.next()
#     a.close()


