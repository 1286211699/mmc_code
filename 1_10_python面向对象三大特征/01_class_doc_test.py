#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 21:17
# @Author  : Xuegod Teacher For
# @File    : 01_class_doc_test.py
# @Software: PyCharm
'''
10.1  类的内置属性和方法
10.1.1  类的内置属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

'''


class People:
    '''
    所有人类的基类
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def set_info(self):
        print('set_info')

    def print_info(self):
        print(self.name,self.age)


po = People('for',18)

po.print_info()
print('类的属性',po.__dict__)
#以字典的形式打印出说有是属性
print('类的属性',People.__dict__)
print('类的属性',People.__doc__)
print('类的属性',People.__name__)
print('类的属性',People.__bases__)
