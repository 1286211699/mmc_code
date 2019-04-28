#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 21:47
# @Author  : Xuegod Teacher For
# @File    : 05_jecheng_test.py
# @Software: PyCharm
# class Animal:
#     def __init__(self,name = '动物',color = '黄色'):
#         self.__name = name
#         self.color = color
#     def eat(self):
#         print('吃……')
#     def drink(self):
#         print('喝……')
#     def __test(self):
#         print(self.color)
# class Dog(Animal):
#     def eat(self):
#         print('狗吃……')
#     def call(self):
#         print('汪汪叫……')
#     def test01(self):
#         print(self.__name)
# class Cat(Animal):
#     def catch(self):
#         print('抓老鼠……')
#
# dog = Dog()
# dog.test01()

class Base(object):
    def __init__(self):
        print('base')
    def test(self):
        print('base_test')
class A(Base):
    def __init__(self):
        print('A')
    # def test1(self):
    #     print('test1')
class B(Base):
    def __init__(self):
        print('B')
    def test(self):
        print('test2')
class C(A,B):
    pass
c = C()
c.test()
print(c.__class__.__mro__)













