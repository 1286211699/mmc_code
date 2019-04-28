#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 20:41
# @Author  : Xuegod Teacher For
# @File    : 01_func_test.py
# @Software: PyCharm
# def func(a):
#     print('for is cool')
#     return a+1
# # print(func)
# # print(func(8))
# a = func(8)
# print(a)





# def func(name,city):
#
#     print("I am %s,I am from %s"%(name,city))
#
# func('for','xuegod')
# func('xuegod','for')




# def func(name,city):
#
#     print("I am %s,I am from %s"%(name,city))
#
# func(name='for',city='xuegod')
# func(city='xuegod',name='for')



# def func(name,city='beijing'):
#
#     print("I am %s,I am from %s"%(name,city))
#
# func('for')
#
# func('for','xuegod')

# def say_hello(*args):
#     print(args)
# say_hello()
# say_hello(1)
# say_hello(1,2,3,4,5)


# def say_hello(**kwargs):
#     print(kwargs)
# say_hello()
# say_hello(a =1 )
# say_hello(a =1,b=2,c=3)


def say_hello(e,f,p = 2,*args,**kwargs):
    a = args
    b = kwargs
    print(a,b)
say_hello(1,2,3,a=1)










