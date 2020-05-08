#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 21:05
# @Author  : Xuegod Teacher For
# @File    : 06_many_test.py
# @Software: PyCharm

class Base(object):
    def __init__(self):
        print('ba')
    def test(self):
        print('base')

class B(Base):
    def __init__(self):
        print('B')
    def test1(self):
        print('test1')

class A(Base):
    def __init__(self):
        print('A')
    def test2(self):
        print('test2')

class C(B,A):
    # def __init__(self):
    #     print('c')
    pass

c = C()
c.test()
# c.test1()
# c.test2()
#继承的顺序是先广度后深度
# print(c.__class__.__mro__)
'''
新式类，只执行一次初始化函数
说明：
1.  python中是可以多继承的并且父类中的方法、属性，子类也都会继承
2.  python3中的多继承遵循mro算法顺序当中的，先广度后深度的原理。
3.  新式类只会执行一次__init__()文件
# 3层封装
10.3.5  继承总结
子类在继承的时候，在定义类时，小括号()中为父类的名字。
子类继承后，父类的属性、方法，都会被继承给子类。
私有的属性，不能通过对象直接访问，但是可以通过方法访问。
私有的方法，不能通过对象直接访问。
私有的属性、方法，不会被子类继承，也不能被访问。
'''

