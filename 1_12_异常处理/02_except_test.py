#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 16:05
# @Author  : Xuegod Teacher For
# @File    : 02_except_test.py
# @Software: PyCharm
print('---start----')
try:
    print(name)
    open('123.txt','r')
    print('---try----')
except:
    print('有异常，但是哥哥就不想打印……')
# except (NameError,FileNotFoundError,TypeError):
#     print('这是一个NameError的错误%s'%NameError)
#     print('这是一个FileNotFoundError的错误%s'%FileNotFoundError)
#     print('这是一个TypeError的错误%s'%TypeError)
print('---end----')
