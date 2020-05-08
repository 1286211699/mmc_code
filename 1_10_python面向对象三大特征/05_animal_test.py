#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 20:53
# @Author  : Xuegod Teacher For
# @File    : 05_animal_test.py
# @Software: PyCharm
'''
私有的属性，私有方法,不能被继承
'''
class Animal:
    def __init__(self,name='动物',color = '黄色'):
        self.__name = name
        self.color = color
    def eat(self):
        print('eat')
    def drink(self):
        print('drink')

class Dog(Animal):
    def call(self):
        print('小狗叫……')
    #方法的重写
    def eat(self):
        print('狗吃……')

    def hello(self):
        print(self.__name)

class Cat(Animal):
    def catch(self):
        print('抓老鼠……')

lucky = Dog()
lucky.call()
lucky.drink()
lucky.eat()
# print(lucky.color)
lucky.hello()