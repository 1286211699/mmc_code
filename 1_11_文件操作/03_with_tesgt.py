#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:37
# @Author  : Xuegod Teacher For
# @File    : 03_with_tesgt.py
# @Software: PyCharm
# class A:
#     def __enter__(self):
#         print('__enter__() is called')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__() is called')
# with A() as a:
#     print('got instance')



with open('for.png','rb') as png1:

    with open('0.jpg','wb') as png2:

        png2.write(png1.read())

with open('for.png','rb') as png1,open('0.jpg','wb' )as png2:
    png2.write(png1.read())








