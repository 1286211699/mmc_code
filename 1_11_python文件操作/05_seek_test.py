#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 21:49
# @Author  : Xuegod Teacher For
# @File    : 05_seek_test.py
# @Software: PyCharm
'''
1.获取当前指针的位置tell
2. seek() 控制指针位置
seek()方法用于移动文件读取指针到指定位置。
seek()语法格式：fileObject.seek(offset[, whence])
seek [siːk]: 寻找
whence [wens]: 从何处;从哪里
offset [ˈɒfset]: 抵消;弥补;补偿
offset   移动的长度（字节）
whence  相对位置；0从开头（默认），1从当前，2从末尾
如果offset为负数，表示从后往前移动n个字节


'''

with open('test.py','r',encoding='utf-8') as f:
    #读取的时候是字符
    print(f.read(5))
    #偏移量谨慎使用。字节形式
    f.seek(1,0)
    print(f.read(5))

    #这是告诉我指针的位置，返回的什么结果：字节
    # print(f.tell())