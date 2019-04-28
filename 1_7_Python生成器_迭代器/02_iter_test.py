#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 20:51
# @Author  : Xuegod Teacher For
# @File    : 02_iter_test.py
# @Software: PyCharm
# a = 'abcdef'
#
# # for i in a:
# #     print(i)
#
# b = iter(a)#转换为迭代器
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# # for i in b:
#     print('这是一个next',i)

L = [2,3,5,7]

# for x in L:
#     print(x)
# else:
#     print('循环结束')


#
# it = iter(L)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         print('循环结束')
#         break
it = iter(L)
n = 0
while n < len(L):
    print(next(it))
    n += 1
else:
    print('循环结束')








