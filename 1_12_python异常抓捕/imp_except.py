#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 22:21
# @Author  : Xuegod Teacher For
# @File    : imp_except.py
# @Software: PyCharm
# 多重封装
class MyException(Exception):
    def __init__(self,num,atleast):
        super().__init__()
        self.num = num
        self.atleast = atleast