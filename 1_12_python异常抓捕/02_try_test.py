#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 21:41
# @Author  : Xuegod Teacher For
# @File    : 02_try_test.py
# @Software: PyCharm
'''
12.2.1  捕获异常
语法格式：
try:
可能触发异常的语句块
except [exceptionType]:
   捕获可能触发的异常[可以指定处理的异常类型]
except [exceptionType]:
    捕获异常并获取附加数据

'''
'''
你们能保证你编写的代码？python 之父,
程序不爆错 就是最大错误？
从上往下执行，无论如何只会抓捕到第一错误,
如何抓捕多个异常？
try里面有多个异常，100之中的一种，我都能给你抓捕
'''

print('------start-------')
try:

    print(name) #NameError
    open('1.txt') #FileNotFoundError
    print('---try----')
#万金油第一种，常用的

except Exception as e:
    print('错误 %s'% e)


#不提倡
# except (FileNotFoundError,NameError,ImportError):
#     print('FIle错误%s'%FileNotFoundError)
#     print('FIle错误%s'%NameError)
#     print('FIle错误%s'%ImportError)

# except NameError:
#     print('Name 错误%s'%NameError)
#第三种
# except:
#     print('错误')

print('------end-------')
