#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 16:08
# @Author  : Xuegod Teacher For
# @File    : 02_tuple_test.py
# @Software: PyCharm
# num = (11,22,33,'aa')

# num = 1,2,3,'a'

# num = (1,2,3,'a')
#
# print(num[1])
# # print(type(num))


# num = (1,'a',[1,2])
#
# num[1] = 2
# print(id(num))
# num[2].append(3)
# print(id(num))
# print(num)

# num = [1,2,3,4,5]
# str1 = 'hello'
# num2 = tuple(str1)
# print(''.join(num2))

tup2 = (0,1,2,3,4,5,5,6)
print(tup2.index(1))
print(tup2.count(5))