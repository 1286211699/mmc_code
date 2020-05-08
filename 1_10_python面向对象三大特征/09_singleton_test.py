#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 22:16
# @Author  : Xuegod Teacher For
# @File    : 09_singleton_test.py
# @Software: PyCharm
#if __私有方法属性
class SingLeton(object):
    #私有的类属性是不是已经给该
    __instance = None
    __first_init = False
    def __new__(cls,name, age):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


    def __init__(self,name,age):
        if not self.__first_init:
            self.name = name
            self.age = age
            SingLeton.__first_init = True
a = SingLeton('for',19)
b = SingLeton('json',20)
print(b.name,b.age)
# print(a.name)
# print(b.name)
# a.age  = 19
print(id(a))
print(id(b))
# print(b.age)