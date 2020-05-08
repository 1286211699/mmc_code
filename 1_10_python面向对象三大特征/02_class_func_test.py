#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 21:26
# @Author  : Xuegod Teacher For
# @File    : 02_class_func_test.py
# @Software: PyCharm
'''
10.1.2  类方法
	1.  类方法
类方法是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法.
类方法能不能更改类属性？可以的 内部修改

2. 静态方法 @staticmethod,
'''
class People(object):

    country = 'china'

    @classmethod #类方法
    def __get_country(cls):
        return cls.country

    @classmethod
    def __set_country(cls,c):
        cls.country = c


    #静态方法主要是控制逻辑的
    @staticmethod
    def order_info():
        People.__set_country('for')
        return People.__get_country()
#
#
p = People()
# print(People.__class__.__mro__)
# print(p.__get_country())
# print(People.get_country())
# People.__set_country('beijing')
# # print(People.get_country())
# print(p.order_info())
# print(data)

# import time
# import requests
#底层代码编写，知道一些方法 的具体使用就OK了
import json
# player_name = 'for'/

class Game(object):

    player_name = '111'
    #
    def __init__(self,player_name):
        self.player_name = player_name
        Game.show_help()
        Game.show_top()

    @staticmethod
    def show_help():
        print('-----------')
        print('查看帮助信息')
        print('-----------')

    @classmethod
    def show_top(cls):
        print('----------')
        print('最高分:1111')
        print('----------')

    def start_game(self):
        print('%s 开始游戏'%self.player_name)

if __name__ == '__main__':

    g = Game('for')
    g.start_game()










