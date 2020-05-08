#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 22:16
# @Author  : Xuegod Teacher For
# @File    : 04_raise_test.py
# @Software: PyCharm
'''
12.4  触发异常
你可以用raise语句来引发一个异常，异常/错误对象必须有一个名字，且它们应是Error或Exception类的子类，我们可以使用raise语句自己触发异常。
raise语法格式如下：
raise [Exception [, args [, traceback]]]
语句中 Exception 是异常的类型（例如，NameError）参数标准异常中任一种，args 是自已提供的异常参数。
最后一个参数是可选的（在实践中很少使用）跟踪异常对象（了解一下）。
抛出异常后，raise  后面的代码不再执行，为了能够捕获异常，"except"语句必须要用相同的异常来抛出类对象或者字符串。

'''


class MyTest(object):

    def start(self):

        try:
            content = int(input('请输入一个数字:'))

            if content < 5:

                raise FileNotFoundError('你输入的数字小于5')

        except FileNotFoundError as e:

            print(e)

        else:
            print('success')

if __name__ == '__main__':
    t = MyTest()
    t.start()