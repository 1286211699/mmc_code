#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 21:16
# @Author  : Xuegod Teacher For
# @File    : 04_pro_test.py
# @Software: PyCharm
import multiprocessing,time

my_list = []

def write_data():
    for i in range(5):
        my_list.append(i)
        time.sleep(0.2)
    print('write_data:',my_list)

def read_data():
    print('read_data:',my_list)

if __name__ == '__main__':
    write_process = multiprocessing.Process(target=write_data)
    read_process = multiprocessing.Process(target=read_data)
    #主进程等待写入程序执行完成之后，再继续往下执行
    write_process.start()
    write_process.join()


    read_process.start()