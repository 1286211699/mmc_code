#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 21:28
# @Author  : Xuegod Teacher For
# @File    : 04_jiu_test.py
# @Software: PyCharm
# 1 x 1 = 1
# 1 x 2 = 2  2 x 2 = 4
# 1 x 3 = 3  2 x 3 = 6 3 x 3 = 9

for i in range(1,10):
    # print('这个是外层循环:',i)
    for j in range(1,i+1):
        print('%d x %d = %d'%(j,i,i*j),end='-')
    print()