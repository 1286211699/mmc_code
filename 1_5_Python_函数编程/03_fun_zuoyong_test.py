#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 22:08
# @Author  : Xuegod Teacher For
# @File    : 03_fun_zuoyong_test.py
# @Software: PyCharm
# import sys
# print(dir(sys))
#全局
# name = 'while'#全局变量
# def outer():
#     # nonlocal name
#     name = 'for'#嵌套变量
#     def inner():
#         # global name
#         # nonlocal name
#         name = 'for is cool'#本地变量
#         age = 18
#         print(name)
#         print(age)
#     inner()
#     print(name)
# outer()
# print(name)
#
# c = [1,2,3]
# d = {}
# e = set()
#
# def test01():
#     c.append('5')
#     d.update({'mame':'for'})
#     e.add(1)
# test01()
# print(c,d,e)


import functools
def add(a,b):
    return  a+b
plus3 = functools.partial(add,3)
plus5 = functools.partial(add,5)
print(plus3(2))
print(plus5(3))











