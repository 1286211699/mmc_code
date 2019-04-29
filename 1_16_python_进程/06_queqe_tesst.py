#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 21:52
# @Author  : Xuegod Teacher For
# @File    : 06_queqe_tesst.py
# @Software: PyCharm
import multiprocessing
import time
if __name__ == '__main__':
    queue = multiprocessing.Queue(3)

    #放入数据
    queue.put(1)
    queue.put('hello')
    queue.put([3,5])

    queue.empty()#不太可靠
    #加延时操作
    #使用个数qszie不适用empty()
    if queue.qsize() == 0:
        print('队列为空')
    else:
        print('队列不为空')
    #
    size = queue.qsize()
    print(size)

    value = queue.get()
    print(value)
    value = queue.get()
    print(value)
    value = queue.get()
    print(value)

    value =  queue.get_nowait()
    print(value)
    # size = queue.qsize()
    # print(size)

