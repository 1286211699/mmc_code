#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 20:47
# @Author  : Xuegod Teacher For
# @File    : 01_mult_process_test.py
# @Software: PyCharm
import multiprocessing
import time
def run_proc():
    '''子进程要执行的代码'''
    while True:
        print('---2----')
        time.sleep(1)
if __name__ == '__main__':
    #创建一个子进程
    sub_process = multiprocessing.Process(target=run_proc)
    #开启一个子进程
    sub_process.start()
    while True:
        print('---1---')
        time.sleep(2)