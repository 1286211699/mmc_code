#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 21:01
# @Author  : Xuegod Teacher For
# @File    : 02_read_test.py
# @Software: PyCharm
'''
读取文件
1.文件的对象是可迭代对象
2. 讲解这个方法之前 如果我for 给你一个100g文件，你用什么方法打开？
# open（）read() 能一下读取100G boom

3. readline() readlines() #读取一行
'''
#python3  wind gbk
f = open('test.py','r',encoding='utf-8')
#添加的size 汉字3-5 6个字节，字符
# print(f.read(5))
# print(f.read(5))

# print(f.readline())
print(f.readlines())


# print(f)
# #通过for循环可以获取到文件对象中的每一行
# for i in f:
#     print(i)

f.close()
