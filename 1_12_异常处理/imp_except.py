#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 16:44
# @Author  : Xuegod Teacher For
# @File    : imp_except.py
# @Software: PyCharm
class MyException(Exception):
    def __init__(self,num,atleast):
        super().__init__()
        self.num = num
        self.atleast = atleast

