#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 15:19
# @Author  : Xuegod Teacher For
# @File    : 05_os_test.py
# @Software: PyCharm
#os.path.join
# import os
# # E:\xuegod_code\1_11_文件操作\1.txt
# file_path = os.getcwd()
# # print(file_path)
# new_path = os.path.join(file_path,'1.txt')
# print(new_path)
#

# import os
# path = os.getcwd()
#
# for root,dirs,files in os.walk(path):
#     for filename in files:
#         print(os.path.join(root,filename))



import os
m_name = os.listdir('。/xuegod/')

for temp in m_name:

    new_name = 'xuegod_' + temp

    os.rename('./xuegod/'+temp,'./xuegod/'+new_name)
