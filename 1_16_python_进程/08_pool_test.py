#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 22:16
# @Author  : Xuegod Teacher For
# @File    : 08_pool_test.py
# @Software: PyCharm
import multiprocessing
import time

def work():
    print('复制中……',multiprocessing.current_process().pid)
    time.sleep(0.5)
if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(5):
        pool.apply(work)
    pool.close()
    pool.join()

