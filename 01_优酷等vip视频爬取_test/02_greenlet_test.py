#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 10:12
# @Author  : Xuegod Teacher For
# @File    : 02_greenlet_test.py
# @Software: PyCharm
import time
import greenlet
def work1():
    for i in range(5):
        print('---work01---')
        time.sleep(0.2)
        g2.switch()
def work2():
    for i in range(5):
        print('----work02---')
        time.sleep(0.2)
        g1.switch()
if __name__ == '__main__':
    #创建协程指定任务
    g1 = greenlet.greenlet(work1)
    g2 = greenlet.greenlet(work2)
    #开启一个协程任务
    g1.switch()