# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 16:30
# @Author  : for 
# @File    : 06_pass_test.py
# @Software: PyCharm
name = 'xuegod'

for i in name:
    if i == 'e':
        pass
    print(i,end=' ')


#
name = 'xuegod'

for i in name:
    if i == 'e':
        continue
    print(i,end=' ')

i = 0
while i < 10:
    i = i + 1

    if i == 5:
        continue
    print(i,end=' ')












