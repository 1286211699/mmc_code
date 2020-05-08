#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 22:07
# @Author  : Xuegod Teacher For
# @File    : 03_except_else.py
# @Software: PyCharm

'''
else : 是和except对应的，没有错误会执行else
用好了事半功倍，代码设计的流程，慢慢的填充

finally：
'''
# a = 1
try:
    print(a)
    # open('1.txt')

except Exception as e:
    print(e)

else:
    print('else')

finally:
    print('finally')

