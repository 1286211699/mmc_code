#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 15:31
# @Author  : Xuegod Teacher For
# @File    : 07_mageic_test.py
# @Software: PyCharm
# class Hero:
#     def __del__(self):
#         print('英雄已经阵亡')
#
# man1 = Hero()
# man2 = man1
# del man1
# del man2
# print('程序结束')

# class A(object):
#     def __init__(self,name,age):
#         print('这是init方法')
#         self.name = name
#         self.age = age
#     def __new__(cls, name,age):
#         print('这是new方法')
#         return object.__new__(cls)
# a = A('for',18)
# print(a.name)





class Test(object):
    def __init__(self,world):
        self.world = world
    def __str__(self):
        print('--str---')
        return 'world is %s'%self.world
t = Test('for')
print(t)



