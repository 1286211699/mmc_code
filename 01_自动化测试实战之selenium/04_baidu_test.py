#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 12:47
# @Author  : Xuegod Teacher For
# @File    : 04_baidu_test.py
# @Software: PyCharm
import threading
import time
def run(number):
    print('%s…… starting '%number)
    time.sleep(2)
    print('____________')
if __name__ == '__main__':
    print('___主线程开始___',threading.current_thread().name)
    thread_list=[]
    for i in range(1,5):
        #创建，实例化一个线程
        t = threading.Thread(target= run,args=(i,))
        thread_list.append(t)
    #将实例化的线程都放到列表中，统一执行
    for t in thread_list:
        t.start()
        # t.join()
    for i in thread_list:
        i.join()
    print('___主线程结束___',threading.current_thread().name)
