#!/usr/bin/python
# coding=utf-8
# __author__='dahu'
# data=2017-
# queue 热身

import Queue

q = Queue.Queue(maxsize=5)

for i in range(5):
    q.put(i)

# while not q.empty():
#     print q.get()
    # q.join()
    # print 'hehe'

q = Queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()


#优先级队列
import Queue
import threading
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'Job:',description
        return
    def __cmp__(self, other):           #需要加上这个比较函数,
        return cmp(self.priority, other.priority)   #Return negative if x<y, zero if x==y, positive if x>y.

q = Queue.PriorityQueue()

q.put(Job(3, 'mid-level job'))
q.put(Job(10, 'low-level job'))
q.put(Job(1, 'high-level job'))

def process_job(q):
    while True:
        next_job = q.get()
        print 'for:', next_job.description
        q.task_done()

workers = [threading.Thread(target=process_job, args=(q,)),
        threading.Thread(target=process_job, args=(q,))
        ]

for w in workers:
    w.setDaemon(True)   #守护进程
    w.start()

q.join()