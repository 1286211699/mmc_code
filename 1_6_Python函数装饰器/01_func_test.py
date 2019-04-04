#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 20:33
# @Author  : Xuegod Teacher For
# @File    : 01_func_test.py
# @Software: PyCharm
# def fun1():
#     print('this is fun1')
#
# def fun2():
#     print('this is fun2')
#
# def main():
#     fun1()
#     fun2()
#
# main()

# 2、 递归函数的使用
# 举个例子：
# 我们来计算阶乘 n! = 1 * 2 * 3 * ... * n

# a = sum(range(1,101))
# print(a)

# n = int(input('请输入一个数字:'))
# result = 1
# i = 1
# while i <= n:
#     #i = 1, i = 2
#     result = result * i # 1,2,6
#     i += 1
# print(result)
# 紧接着我们看下阶乘的规律：
# 1! = 1
# 2! = 2 × 1 = 2 × 1!
# 3! = 3 × 2 × 1 = 3 × 2!
# 4! = 4 × 3 × 2 × 1 = 4 × 3! ...
# n! = n × (n-1)!
# def test(n):
#     if n == 1:
#         return 1
#     return n * test(n-1)#3 * test(2)  ,test(2) == 2 * 1  3*2*1
# while True:
#     # n = 3
#     n = int(input('请输入你想要的数字:'))
#     # test(3)
#     print(test(n))


# 3、递归函数经典案例（面试）：
# 题目：斐波那契数列，该数列中有n个数字，1 1 2 3 5 8
# 分析：该数列中，从第三个数字开始：数值 = 前一个数字 + 前 前面一个数字


# def feibo(n):
#     a,b = 0,1
#     c = []
#     while n > 0:
#         c.append(b)
#         a,b = b,a+b
#         n -= 1
#     print(c)
# feibo(10)

# def feibo(n):
#     if n <= 1:
#         return 1
#     elif n == 2:
#         return 1
#     return feibo(n-1)+feibo(n-2)
# n = int(input('>>>'))
# a = [feibo(i)for i in range(1,n+1)]
# print(a)




def func_test(n):
    return test(n,1)
def test(num,product):
    if num == 1:
        return product
    return test(num-1,num*product)
print(func_test(5))