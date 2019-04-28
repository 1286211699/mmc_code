#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 10:55
# @Author  : Xuegod Teacher For
# @File    : test.py
# @Software: PyCharm
def my_zip(*args):
    #定义一个空列表
    all_list = []
    for i in range(len(args)):
        all_list.append(args[i])
    # all_list = [i for i in range(len(args))]
    print('这是all_list:',all_list)
    # 排序的两种方法
    sort_list = sorted(all_list,key=lambda x: len(x))
    print('这是排序结果:',sort_list)
    #最小的长度
    min_list_longth = len(sort_list[0])
    # min_list_longth = min([len(i) for i in all_list])
    #定义一个空列表
    a_list = []
    for a in range(min_list_longth):
        a = [args[j][a] for j in range(len(args))]
        a_list.append(a)
    print(a_list)

my_zip('abc','abcd')
