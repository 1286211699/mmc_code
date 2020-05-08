#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 22:23
# @Author  : Xuegod Teacher For
# @File    : taise_test.py
# @Software: PyCharm

from imp_except import MyException


class MyTest(object):

    def start(self):

        try:
            content = int(input('请输入一个数字:'))

            if content < 5:

                raise MyException(content,3)

        except MyException as e:

            print(e.num,e.atleast)

        else:
            print('success')

if __name__ == '__main__':
    t = MyTest()
    t.start()