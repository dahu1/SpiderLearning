#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#data=2017-
# 中文每行一个字,英文每行一个词,awk不大好操作
#示例:
#    导航去hello kitty乐园
#
#      导
#      航
#      去
#      hello 
#      kitty
#      乐
#      园
#      .
#
import re,sys
reload(sys)
sys.setdefaultencoding('utf8')
def process(filename):
    with open(filename,'r')as f:
        for line in f:
            yield line
if __name__ == '__main__':
    gen=process('tmp')
    for line in gen:
        if re.search('^[^"].*\w',line) or re.search('^\w',line):
            print line,
            a=[]
            b=line.strip().decode('utf-8')  #解码,技巧,用len查看string,根据大小来判断是否要加解码
            # print [i for i in b]
            for i in b: #本来想直接列表推导,但是好像不支持条件判断
                if re.search('\w',i):
                    a.append(i)
                elif i==' ':
                    a.append(i)
                else:
                    a.append(i+'\n')
            line=''.join(a)
            for m in re.finditer('\w+',line):
                # print m.span(),m.group(),line[m.start():m.end()]  #温故一下
                line=line.replace(m.group(),m.group()+'\n')
            line=''.join([i.strip()+'\n' for i in line.split('\n') if i!=''])    #去除空格
            # print [i for i in line]  #列表查看下,可以看清楚每个字节到底是什么
            print line,
            break
        # else:
        #     print line,


