#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
#直接看堆栈信息了
import sys
import inspect
def aa():
    return inspect.stack()

print aa.__name__,getattr(aa,'__name__')
def hehe(a):
    print a
    print aa()
hehe(5)


def get_current_function_name():
    return inspect.stack()[1][3]
class MyClass:
    def function_one(self):
        print get_current_function_name()
        print "%s.%s invoked"%(self.__class__.__name__, get_current_function_name())
if __name__ == "__main__":
    myclass = MyClass()
    myclass.function_one()