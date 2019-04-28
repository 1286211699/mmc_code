#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 16:48
# @Author  : Xuegod Teacher For
# @File    : 06_def_try_test.py
# @Software: PyCharm
def test01():
    print('---start---')
    print(num)

def test02():
    print('---test02')

def test03():
    try:
        print('---test03----')
        test01()
    except Exception as e:
        print(e)
if __name__ == '__main__':
    test03()