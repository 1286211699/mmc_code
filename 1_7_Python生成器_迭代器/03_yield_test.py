#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:15
# @Author  : Xuegod Teacher For
# @File    : 03_yield_test.py
# @Software: PyCharm
# def my_yield():
# #     print('即将生成2')
# #     yield 2
# #     print('即将生成3')
# #     yield 3
# #     print('即将生成5')
# #     yield 5
# #     print('即将生成7')
# #     yield 7
# #     print('生成结束')
# #
# # gen = my_yield()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))


# gen = (x**2 for x in range(1,5))
# print(list(gen))

L = [2, 3, 5, 7]
# a = map(lambda x:x*x,L)
# print(list(a))

# L2 = [i ** 2 for i in L]
#
# print(L2)


G3 = ( i ** 2 for i in L)
# print(list(G3))
print(next(G3))
print(next(G3))
print(next(G3))




















