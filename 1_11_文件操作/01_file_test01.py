#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 14:45
# @Author  : Xuegod Teacher For
# @File    : 01_file_test01.py
# @Software: PyCharm

# f = open(r'E:\xuegod_code\1_11_文件操作\1.txt','r',encoding='utf-8')
# # print(f.read(10))
# # print(f.read(10))
# # print(f.read(10))
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# print(f.readlines())

# f.close()

# for i in f:
#     print(i)

# print(r'abc\ndef')




# f = open('2.py','a',encoding='utf-8')
#
# f.write('你好啊,hello world')
# f.write('你好啊,hello world')
# f.write('你好啊,hello world')
# f.write('你好啊,hello world')
#
# f.close()

# with open('1.txt','r',encoding='utf-8') as f:
#     print(f.read())
#
# print(f.closed)




class A():
    def __enter__(self):
        print('__enter__() is called')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__() is called')
with A() as a:
    print('got instance')


