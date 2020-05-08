#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 21:22
# @Author  : Xuegod Teacher For
# @File    : 04_with_test.py
# @Software: PyCharm
#with 和的意思 可以自动打开课关闭文件
# with open('1.txt') as f:
#     print(f.read())
#
# print(f.closed)

# class A:
#
#     def __enter__(self):
#         print('enter')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#
# with A() as a:
#     print('test')
#pip install requests
# import requests
# #临时加的
# response = requests.get('https://p3.ssl.qhimgs1.com/sdr/400__/t01a9f7f11254e3cffd.jpg')
#
# with open('1.jpg','wb') as f:
#
#     f.write(response.content)

'''
with变形
'''
#方法比较好理解
# with open('1.jpg','rb') as jpg1:
#     with open('2.jpg','wb') as jpg2:
#         jpg2.write(jpg1.read())
#不推荐
# with open('1.jpg','rb') as jpg1, open('2.jpg','wb') as jpg2:
#     jpg2.write(jpg1.read())




