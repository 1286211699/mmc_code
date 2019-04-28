#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 22:06
# @Author  : Xuegod Teacher For
# @File    : 03_init_test.py
# @Software: PyCharm

# class Cat():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         # print('__init__被调用')
#     def eat(self):
#         pass
#     def drink(self):
#         pass
#     def print_info(self):
#         print('%s的年龄是%s'%(self.name,self.age))
# tom = Cat('汤姆',18)
# tom.print_info()
# #
# lucky = Cat('幸运',18)
# lucky.print_info()



class Cat():

    def __init__(self,*args,**kwargs):
        self.data1 = args
        self.data2 = kwargs
    def print_info(self):
        print(self.data1)
        print(self.data2)
tom = Cat(1,2,3,a=1)
tom.print_info()

# map()












