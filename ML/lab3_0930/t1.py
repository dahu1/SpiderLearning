#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
import kNN
testVector = kNN.img2vector('digits/testDigits/0_1.txt')
print testVector[0,0:31]