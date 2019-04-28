#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 20:46
# @Author  : Xuegod Teacher For
# @File    : 02_classmethod_test.py
# @Software: PyCharm
# class People(object):
#
#     country = 'china'
#
#     @classmethod#类方法
#     def getCountry(cls):
#         return  cls.country
#     @classmethod
#     def setCountry(cls,country):
#         cls.country = country
# p = People()
# print(p.getCountry())
# print(People.getCountry())
# print('----------------')
# p.setCountry('japan')
# print(p.getCountry())
# print(People.getCountry())
# # People.test(p)




class People(object):

    @staticmethod#类方法
    def getCountry():
        print('I come from china')
People.getCountry()

P = People()#实例一个对象
P.getCountry()



