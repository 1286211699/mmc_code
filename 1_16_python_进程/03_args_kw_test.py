#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 21:07
# @Author  : Xuegod Teacher For
# @File    : 03_args_kw_test.py
# @Software: PyCharm
import multiprocessing
def show_info(name,age):
    print(name,age)
    corrent_process = multiprocessing.current_process()
    print(corrent_process.name)
if __name__ == '__main__':
    # sub_process = multiprocessing.Process(target=show_info,name = 'myprocess',args=('for',))
    sub_process = multiprocessing.Process(target=show_info,name = 'myprocess')
    sub_process.start()


