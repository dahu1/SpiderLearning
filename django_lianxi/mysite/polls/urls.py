#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]