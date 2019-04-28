#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 16:37
# @Author  : Xuegod Teacher For
# @File    : 04_raise_test.py
# @Software: PyCharm

from imp_except import MyException

class Test(object):
    def start(self):
        try:
            content = int(input('请输入一个数字:'))
            if content < 5:
                raise MyException(content,5)
        except MyException as info:
           print('当前大小为：%s 最小的数字为:%s'%(info.num,info.atleast))
        else:
            print('恭喜你没有异常')
t = Test()
t.start()