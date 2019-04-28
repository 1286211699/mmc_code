#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 16:46
# @Author  : Xuegod Teacher For
# @File    : 05_tyr_test.py
# @Software: PyCharm
import time
try:
    f = open('123.txt',encoding='utf-8')
    try:
        while True:
            for i in range(3):
                print(f.readline())
            time.sleep(2)
            content = f.readline()
            print(content)
            if len(content) == 0:
                break
    finally:
        f.close()
except:
    print('没有这个文件')