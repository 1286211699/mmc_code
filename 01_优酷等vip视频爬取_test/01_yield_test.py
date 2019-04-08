#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 10:07
# @Author  : Xuegod Teacher For
# @File    : 01_yield_test.py
# @Software: PyCharm
import time
def work1():
    while True:
        print('---work01---')
        yield
        time.sleep(1)
def work2():
    while True:
        print('---work02---')
        yield
        time.sleep(0.5)

def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)
if __name__ == '__main__':
    main()