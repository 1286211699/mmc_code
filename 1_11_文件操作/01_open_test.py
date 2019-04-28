#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:08
# @Author  : Xuegod Teacher For
# @File    : 01_open_test.py
# @Software: PyCharm
f = open('1.txt','r')
#判断文件是否关闭
print(f.closed)
#查看文件的权限
print(f.mode)
#差看文件的name
print(f.name)
#关闭文件
f.close()