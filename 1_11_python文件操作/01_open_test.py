#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 20:38
# @Author  : Xuegod Teacher For
# @File    : 01_open_test.py
# @Software: PyCharm
'''
path
文件路经: 前期的时候我们写成固定的（绝对和相对路经），也可以使用os模块来辅助完成
mode权限: r（read）读权限，w（write）写权限，a（add）追加写
buffering：用于设置缓冲策略的可选整数，缓冲策略包括以下几种类型
0：表示关闭缓冲（仅在二进制模式下允许）
1：选择行缓冲（仅在文本模式下可用），类似命令提示符操作，当按下回车键后，缓冲结束，将回车符前面的内容交给系统进行处理后返回结果。
>1的整数：表示将缓冲区设置为该整数大小。没有参数给定时，执行如下策略：二进制文件的缓冲区大小取决于系统底层设备和操作系统类型，一般情况下为4096或者8192字节长；交互式文本文件（isatty()返回True的文件）使用线路缓冲。其它文本文件使用二进制文件的策略
'''

'''
文件的作用？
记录，log，html logconf
'''
# from .
f = open('1.txt','w+')

print(f.read())
# f.write('123')
#只支持str io str
f.write('123')

print(f.closed)#查看文件有没有关闭
print(f.name) #这是获取文件对象的名字
print(f.mode)#文件对象的权限
f.close()

print(f.closed)

