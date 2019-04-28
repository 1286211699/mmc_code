#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 16:42
# @Author  : Xuegod Teacher For
# @File    : 05_os_test.py
# @Software: PyCharm
# import os
# file_path = os.getcwd()
# new_path = os.path.join(file_path,'1.txt')
# print(new_path)


# print(os.path.getsize('1.txt'))


#
# print('本地路径为',os.getcwd())
#
# path = './xuegod/'
#
# os.chdir(path)
#
# print('新的路径为:',os.getcwd())
#
# os.chdir(r'E:\xuegod_code\1_11_文件操作')


# # E:\xuegod_code\1_11_文件操作\1.txt
# print(os.getcwd())
# print(os.path.isfile('1.txt'))
# print(os.path.isdir('xuegod'))
# print(os.path.exists('1.txt'))
# print(os.path.split(r'E:\xuegod_code\1_11_文件操作\1.txt'))






# import os
# path = os.getcwd()#工作目录
# #返回三元组一个是路径，列表进行包围的目录，所有文件名
# for root,dirs,files in os.walk(path):
#     for filename in files:
#         print(os.path.join(root,filename))
#


#
# import os
#
# m_name = os.listdir('./xuegod/')
# print('文件名',m_name)
# for temp in m_name:
#     new_name = 'xuegod_'+temp
#     # 第一个参数是旧名字，第二个参数是新名字
#     os.rename('./xuegod/'+temp,'./xuegod/'+new_name)




import os
def iterbrowse(path):
    for root,dirs,files in os.walk(path):

        for file in files:
            print(os.path.join(root,file))


new_path = os.getcwd()
iterbrowse(new_path)




