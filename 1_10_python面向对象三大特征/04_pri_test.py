#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 20:36
# @Author  : Xuegod Teacher For
# @File    : 04_pri_test.py
# @Software: PyCharm

class Parent(object):
    #私有的类属性
    __age = 18

    def __init__(self,name):
        #私有的实例属性
        self.__name = name
    #私有实例方法
    def __func(self):
        print('俺是私有的实例方法')

    def hello(self):
        print(self.__age)
        print(self.__name)
        self.__func()


p = Parent('for')
#错误，私有的类属性不能再外部调用
# print(p.__age)
# print(Parent.__age)
# print(p.__name)
p.hello()
# p.__func()
