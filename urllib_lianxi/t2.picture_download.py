#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
#图片下载,用urllib库
import urllib

# fi=urllib.urlretrieve('https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3129311788,3946097352&fm=173&s=B7F45B9569C0514BDA20966C0300B0F5&w=620&h=308&img.JPEG',filename="/home/dahu/PycharmProjects/SpiderLearning/urllib_lianxi/pic.JPEG")
fi=urllib.urlretrieve('https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3129311788,3946097352&fm=173&s=B7F45B9569C0514BDA20966C0300B0F5&w=620&h=308&img.JPEG',filename="t2.pic.JPEG") #位置支持相对位置和绝对位置
urllib.urlcleanup() #清除缓存
