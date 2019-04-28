#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 16:26
# @Author  : Xuegod Teacher For
# @File    : 03_exc_mes_test.py
# @Software: PyCharm
try:
    # num = 10
    print(num)
except Exception as e:
    print('详细信息为%s'%e)
else:
    print('没有发生异常')
finally:
    print('---finally---')