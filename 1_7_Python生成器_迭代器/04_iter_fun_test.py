#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:45
# @Author  : Xuegod Teacher For
# @File    : 04_iter_fun_test.py
# @Software: PyCharm
numbers = [10086, 10000, 10010, 9558]
names = ['中国移动', '中国电信', '中国联通']

# for t in zip(numbers,names):
#     print(t)
# #序列解包赋值
# #x,y = (10086, '中国移动')
# for x,y in zip(numbers,names):
#     print(y,'客服电话是',x)

# def myzip(iter1,iter2):
#     it1 = iter(iter1)
#     it2 = iter(iter2)
#     try:
#         while True:
#             a = next(it1)
#             b = next(it2)
#             yield (a,b)
#     except:
#         pass
# for t in myzip(numbers,names):
#     print(t)
#zip方法
def my_zip(*args):
    # all_list = []#[[1,3],[2,4]]
    # for i in range(len(args)):
    #     all_list.append(args[i])
    all_list = list(args)
    # print(all_list)
    # sort_list = sorted(all_list,key=lambda x:len(x))
    # min_list_logth = len(sort_list[0])
    min_list_length = len(min(all_list,key=lambda x:len(x)))
    a_list = []
    for a in range(min_list_length):
        a = [args[j][a] for j in range(len(args))]
        a_list.append(a)
    print(a_list)
my_zip([1,2,3],[4,2],[1,3,4,5],[1,2,3,4,5,6],[1,3,4,5,6,7])

# a = ['aa','a','aaa']
# print(max(a,key=lambda x:len(x))

# for t in enumerate(names,101):
#     print(t)

def my_enum(iterable,a=0):
    it = iter(iterable)
    i = a
    n = 0
    while n<len(iterable):
        a = next(it)
        yield (i,a)
        i+=1
        n+=1
print(list(my_enum(names,1)))







