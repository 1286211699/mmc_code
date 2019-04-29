#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 21:27
# @Author  : Xuegod Teacher For
# @File    : 05_wait_test.py
# @Software: PyCharm
import multiprocessing,time

def work():
    for i in range(10):
        print('工作中……')
        time.sleep(0.2)
if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    # work_process.daemon = True
    work_process.start()

    time.sleep(1)
    print('主进程执行完毕')
    #
    work_process.terminate()