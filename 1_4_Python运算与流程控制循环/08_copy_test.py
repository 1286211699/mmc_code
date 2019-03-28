# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 17:05
# @Author  : for 
# @File    : 08_copy_test.py
# @Software: PyCharm
import copy

a = [1,2,3,4,[5,6,7]]
b = a
print('a 的 id：%s，b 的id ：%s'%(id(a),id(b)))
c = copy.copy(a)
print('这是个浅copy:',id(c))

d = copy.deepcopy(a)
print('这是个深copy:',id(d))

a.append(8)
a[4].append(9)

print(a)
print(b)
print(c)
print(d)

