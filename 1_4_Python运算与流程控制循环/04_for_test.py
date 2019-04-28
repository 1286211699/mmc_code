#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 16:18
# @Author  : Xuegod Teacher For
# @File    : 04_for_test.py
# @Software: PyCharm
#1*1= 1
#1*2=2 2*2=4
#1*3=3 2*3=6 3*3=9

for i in range(1,10):
    # print('这是外层循环：',i)
    for j in range(1,i+1):
        print('%d x %d = %d\t'%(j,i,i*j),end='')
    print()
