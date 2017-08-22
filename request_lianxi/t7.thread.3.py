#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
#多线程更改变量
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
def consumer():
  r = 'here'
  for i in xrange(3):
    yield r
    r = '200 OK'+ str(i)

c = consumer()
n1 = c.next()
    balance = balance + n
    balance = balance - n

lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance