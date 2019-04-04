#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 21:17
# @Author  : Xuegod Teacher For
# @File    : 02_bibao_test.py
# @Software: PyCharm
# def outer():
#     def inner():
#         print('我是inner')
#     return inner#函数
# f1 = outer()
# f1()

def outer(num):

    def inner(num_in):

        print('inner,num_in is %d'%num_in)

        return num+num_in

    return inner
#a == inner
a = outer(20)
print(a)
# a(200) == inner(200)
print(a(200))
















