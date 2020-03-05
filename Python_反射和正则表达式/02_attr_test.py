#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 20:47
# @Author  : Xuegod Teacher For
# @File    : 02_attr_test.py
# @Software: PyCharm
#中间过渡的
class Test(object):

    pass

if __name__ == '__main__':
    print(hasattr(Test,'name'))
    # if not hasattr(Test,'name'):

    # print(getattr(Test(),'name1'))
    setattr(Test,'age',10)
    print(getattr(Test,'age'))


    # getattr()
    # setattr()
    # print(hasattr(Test,'read'))
    # print(Test.read())