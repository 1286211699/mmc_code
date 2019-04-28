# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 10:29
# @Author  : for 
# @File    : 02_dec_test.py
# @Software: PyCharm

# 等同于 func1 = outer(func1)
#第一个 func1 是为了返回的inner
#第二个 func1 是def func1() 定义的函数，作为一个实参传递给形参 func
def outer(func):
    def inner():
        func()
        print('I come from china')
    return inner
@outer # func1 = outer(func1)
def func1():
    print('this is xuegod1')
if __name__ == '__main__':
    func1()


