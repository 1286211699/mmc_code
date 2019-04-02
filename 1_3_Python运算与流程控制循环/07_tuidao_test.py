#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 22:09
# @Author  : Xuegod Teacher For
# @File    : 07_tuidao_test.py
# @Software: PyCharm
#
# result1 = []
# for i in range(11):
#     result1.append(i)
# print(result1)
#
# result = [ i for i in range(11) if i %2 == 0]
# print(result)

# 那么问题来了，比如现在有一列表L = [[1,2,3],[4,5,6],[7,8,9]]
# 要求出1/4/7  和 1/5/9 元素，思考如何取出？
# L = [[1,2,3],[4,5,6],[7,8,9]]
# result = [i[0] for i in L]
# print(result)
# result1 = [L[i][i]for i in range(len(L))]
# print(result1)
#了解
# a = [(i,j) for i in range(1,5) for j in range(6,10)]
# print(a)
# #展开
# for i in range(1,5):
#     for j in range(6,10):
#         pass
# #还嵌套
# a = [(x,y,z) for x in range(2)for y in range(2)for z in range(2)]
# print(a)


# a = (i for i in range(5))
# for i in a:
#     print(i)