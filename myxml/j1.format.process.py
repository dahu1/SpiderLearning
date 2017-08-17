#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#处理json格式的数据
# with open('c1.json','r') as f:
#     data=json.load(f)
# for i in  data:
#     for j in i:
#         print j,i[j]

#处理jl格式
with open('tieba.kindle.jl','r') as f:
    data=f.readlines()
with open('tieba.kindle.txt','w') as f:
    for i in data:
        item=json.loads(i)
        for j in item:
            print j,'\t',item[j]
            f.write(item[j]+'\n')
data1 = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data1)
