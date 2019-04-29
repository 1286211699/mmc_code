#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 20:56
# @Author  : Xuegod Teacher For
# @File    : 02_pid_test.py
# @Software: PyCharm
import multiprocessing,time,os
def work():
    #获取到当前的进程
    current_process = multiprocessing.current_process()
    #打印当前进程
    print('当前进程',current_process)
    #获取当前进程的编号
    print('当前进程的编号',current_process.pid,os.getpid())
    #获取父进程的编号
    print('父进程的编号',os.getppid())
    #睡两秒
    time.sleep(2)

if __name__ == '__main__':
    #获取主进程
    corrent_process = multiprocessing.current_process()
    #打印下主进程
    print('main:',corrent_process)
    #获取到主进程的编号
    print('main的进程编号',corrent_process.pid)
    #创建一个子进程
    sub_process = multiprocessing.Process(target=work)
    #开启一子进程
    sub_process.start()
    #打印表示
    print('主进程结束')

