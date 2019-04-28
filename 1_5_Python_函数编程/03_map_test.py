#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 21:46
# @Author  : Xuegod Teacher For
# @File    : 03_map_test.py
# @Software: PyCharm
# a = [1,2,3,4]
# b = []
# def func(x):
#     return x*x
# for i in a:
#     b.append(func(i))
# print(b)

#map
# def func(x):
#     return x*x
# # a = map(func,[1,2,3,4])
# # print(list(a))
#
#
# b = map(lambda x:x*x,[1,2,3,4])
# for i in b:
#     print(i)

#
# 练习：给你两个列表a = [1,2,3], b = [4,5,6] 把两者中每个元素的数值相加在一起c=[5,7,9]，你该如何处理？
a = [1,2,3,8]
b = [4,5,6,7]
c = map(lambda x:x%2==0,b)
print(list(c))
# c = map(lambda x,y:x+y,a,b)
# print(list(c))
d = filter(lambda x:x%2==0 and x > 4,b)
print(list(d))

