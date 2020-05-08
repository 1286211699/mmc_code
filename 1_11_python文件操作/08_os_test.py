#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 20:36
# @Author  : Xuegod Teacher For
# @File    : 08_os_test.py
# @Software: PyCharm

import os

# print(os.getcwd())
# print(os.listdir())

#判断当前名字是否在当前目录中是个文件
#三个方法配合什么来使用？ if
# print(os.path.isfile(r'E:\xuegod_code\1_11_Python文件操作\1.txt'))
# print(os.path.isdir('xuegod'))
# print(os.path.exists(r'E:\xuegod_code\1_11_Python文件操作\1.txt'))

'''
split()
'''

# print(os.path.split(r'E:\xuegod_code\1_11_Python文件操作\1.txt'))

# print
#返回的绝对路径
# print(os.path.abspath('1.txt'))

'''
os.path.basename	返回文件名
os.path.dirname	返回文件所在目录
'''
# print(os.path.basename(r'E:\xuegod_code\1_11_Python文件操作\1.txt'))
# print(os.path.dirname(r'E:\xuegod_code\1_11_Python文件操作\1.txt'))

'''
chdir() 修改当前的工作目录，这个方法慎用,有点骚
'''
# print(os.getcwd())
# os.chdir('./xuegod')
# print(os.getcwd())
# os.chdir(r'E:\xuegod_code\1_11_Python文件操作')
# with open('2.txt','w') as f:
#     f.write('111')

'''
os.walk()
'''
# #获取当前的目录
# path = os.getcwd()
# #序列解包赋值,6666666666
# for root,dirs,files in os.walk(path):
#     # print(i)
#     #过滤
#     for file in files:
#         if 'py' in file:
#             print(os.path.join(root,file))

'''
批量修改文件名，rename,
想要修改文件名，首先你要注意你的每个脚本的位置，
'''
# name_list = os.listdir(r'E:\xuegod_code\1_11_Python文件操作\xuegod')
#
# for temp in name_list:
#
#     new_name = 'xuegod_' + temp
#
#     # print(temp)
#     os.rename('./xuegod/' + temp,'./xuegod/' + new_name)


'''
11.4.3  实战：获取文件绝对路径
传入一个文件路径，得到该路径下所有的文件的绝对路径?（面试题）
笔试题
'''

def getPath(path):

    for root,drs,files in os.walk(path):

        for file in files:

            if 'jpg' in file:

                print(os.path.join(root,file))

if __name__ == '__main__':

    path = os.getcwd()

    getPath(path)






