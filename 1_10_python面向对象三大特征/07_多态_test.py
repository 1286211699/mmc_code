#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 21:19
# @Author  : Xuegod Teacher For
# @File    : 07_多态_test.py
# @Software: PyCharm
'''
10.4  方法的重写
10.4.1  重写的概念
我们在学习多态之前我们要学习一下，python中方法的重写，所谓重写，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法。

'''
#以后我们进行方法的重写的时候，别人写好的类,init参数都是固定的原有的参数我肯定不该，自己的封装的时候增加一部分参数
# class Dog(object):
#     # def __init__(self,name,age):
#     #     print(name,age)
#     def print_self(self,name):
#         print('dog')
#         print(name)
#
# class Tom(Dog):
#     # def __init__(self,name,age,adr):
#     #     super().__init__(name,age,adr)
#     #     self.adr = adr
#     #     pass
#     #方法重写
#     def print_self(self,name,age):
#         #super().实例方法名()
#         # super().print_self(name)#关于调用这个父类的方法的时候__init__
#         # super(Tom,self).print_self()
#         # Dog.print_self(self)
#         pass
#
# t = Tom()
# t.print_self('for',18)


'''
10.5  多态
10.5.1  多态定义
多态:(以封装和继承为前提)不同的子类调用相同的方法，产生不同的结果
所谓多态：定义时的类型和运行时的类型不一样，此时就成为多态，更通俗的讲就是多种形态，不同对象调用相同方法的时候产生不同的结果。
注意：Python中主要是通过类的继承以及方法的重写来实现该功能.
作用：
主要用作封装，达到灵活调用的目的、
让编程更加灵活；
提高程序的可拓展性。

'''

# class Dog(object):
#     # def __init__(self,name,age):
#     #     print(name,age)
#     def print_self(self):
#         print('dog')
#         # print(name)
#
# class Tom(Dog):
#     # def __init__(self,name,age,adr):
#     #     super().__init__(name,age,adr)
#     #     self.adr = adr
#     #     pass
#     #方法重写
#     def print_self(self):
#         #super().实例方法名()
#         # super().print_self(name)#关于调用这个父类的方法的时候__init__
#         # super(Tom,self).print_self()
#         # Dog.print_self(self)
#         print('self')
#
# # t = Tom()
# # t.print_self()
# def func(object):
#     object.print_self()
# d = Dog()
#
# t = Tom()
# func(d)
# func(t)
