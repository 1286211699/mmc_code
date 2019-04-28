#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 14:52
# @Author  : Xuegod Teacher For
# @File    : 06_rewrite_test.py
# @Software: PyCharm
class Dog(object):
    def print_self(self):
        print('hello I am dog')

class Tom(Dog):
    def print_self(self):
        # super().print_self()
        # Dog.print_self(self)
        print('Hi I am tom')
def func(object):
    object.print_self()

dog = Dog()
tom = Tom()
func(dog)








