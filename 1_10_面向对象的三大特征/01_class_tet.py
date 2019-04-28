#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 20:34
# @Author  : Xuegod Teacher For
# @File    : 01_class_tet.py
# @Software: PyCharm
class People(object):

    '所有父类的基类'

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def set_info(self):
        print('set_info')

    def print_info(self):
        print(self.name,self.age)

p = People('for',18)
p.print_info()

print('类的属性:',People.__dict__)
print('类的文档字符串:',People.__doc__)
print('类的姓名:',People.__name__)
print('类定义所在模块:',People.__module__)
print('类定义所在模块:',People.__bases__)