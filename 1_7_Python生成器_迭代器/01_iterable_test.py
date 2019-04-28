#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 20:36
# @Author  : Xuegod Teacher For
# @File    : 01_iterable_test.py
# @Software: PyCharm
# a = 'abcdef'
#
# for i in a:
#     print(i)
#
# print(i)



# for i in range(100):
#     print(i)

from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance({1,2,3},Iterable))
print(isinstance({'a':1},Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance(1,Iterable))







