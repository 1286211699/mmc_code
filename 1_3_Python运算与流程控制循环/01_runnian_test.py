#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 20:52
# @Author  : Xuegod Teacher For
# @File    : 01_runnian_test.py
# @Software: PyCharm
year = int(input('请输入一个年份:'))

if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
    print('{}是闰年'.format(year))
else:
    print('{}不是闰年'.format(year))


