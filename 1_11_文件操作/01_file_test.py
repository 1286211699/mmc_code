#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 10:13
# @Author  : Xuegod Teacher For
# @File    : 01_file_test.py
# @Software: PyCharm
# # E:\xuegod_code\1_11_文件操作\1.txt
# f = open(r'E:\xuegod_code\1_11_文件操作\1.txt','r',encoding='utf-8')
#
# # print(f.read(10))
# # print(f.read(10))
#
# # print(f.readline())
# print(f.readlines())
# f.close()


f = open('2.txt','w',encoding='utf-8')
# f.write('你好啊,hello world')
f.writelines([1,2,3])

f.close()











