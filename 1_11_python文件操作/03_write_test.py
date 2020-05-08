#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 21:14
# @Author  : Xuegod Teacher For
# @File    : 03_write_test.py
# @Software: PyCharm
'''

写权限的操作
1.write str
'''
f = open('1.txt','w',encoding='utf-8')

f.writelines(1)
'''
close() 减少我们的资源消耗，保护文件数据 close（）方法后的文件对象是不能操作
'''
f.close()
'''
low
'''
# try:
# #     pass
# # except:
# #     pass
# # finally:
# #     pass


