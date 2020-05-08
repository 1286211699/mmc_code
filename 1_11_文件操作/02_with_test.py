#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 10:44
# @Author  : Xuegod Teacher For
# @File    : 02_with_test.py
# @Software: PyCharm
# with open('2.txt','r',encoding='utf-8') as f:
#     print(f.read())
# print(f.closed)


class A:

    def __enter__(self):
        print('__enter__() is called')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__() is called')

with A() as a:
    print('get instance')













