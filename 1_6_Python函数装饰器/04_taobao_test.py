#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:20
# @Author  : Xuegod Teacher For
# @File    : 04_taobao_test.py
# @Software: PyCharm
import time
a = ['while','for','django']

def outer(func):
    def inner(name):
        func(name)
        print('开始判断你有没有登录')
        time.sleep(2)
        if name in a:
            print('你已经登录，请尽情访问')
            time.sleep(1)
        else:
            print('你没有登录，没有访问权限')
            time.sleep(1)
    return inner
@outer
def goods_cart(name):
    print('%s 要加入购物车'%name)

@outer
def login(name):
    print('%s 要浏览'%name)

# login('fo')

goods_cart('fo')