#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:17
# @Author  : Xuegod Teacher For
# @File    : 02_file_mode_test.py
# @Software: PyCharm
# E:\xuegod_code\1_11_文件操作\1.txt
# f = open('1.txt','r',encoding='utf-8',errors='ignore')
# # print(f.read(10))
# # print(f.read(10))
#
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
#
# # print(f.readlines())
# #对文件进行遍历
# # for i in f:
# #     print(i)
# f.close()


# try:
#
#     f = open('2.txt','w',encoding='utf-8')
#
#     # f.write('你好呀，hello world')
#     f.writelines([1,'b','c'])
#     # f.writelines(str(i) for i in range(10))
# except Exception as e:
#     print(e)
# finally:
#     f.close()
# print(f.closed)


with open('2.txt','r',encoding='utf-8') as f:
    print(f.read())
print(f.closed)










