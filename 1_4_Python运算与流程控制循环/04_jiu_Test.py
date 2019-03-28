# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 16:01
# @Author  : for 
# @File    : 04_jiu_Test.py
# @Software: PyCharm

# 例子：
# 打印九成九乘法：
# 1*1 = 1
# 1*2=2 2*2 = 4
# 1*3=3 2*3=6 3*3 = 9


for i in range(1,10): # i = 2
    for j in range(1,i+1): #j = 1,2
        print('%d x %d = %d\t'%(j,i,i*j),end='')
    print()