# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 21:53
# @Author  : for 
# @File    : 03_str_test.py
# @Software: PyCharm

# print("for's name is"
#       " for")
#
# print('''
# 1
# 2
# 2
# 3
# ''')



# print('abc\ndef')

# %s	字符串占位符
# %d  数字占位符
# %f  浮点型数字占位符
# %.2f  控制浮点型数字占位符
#
# print('My name is %s'%('for'))
# print('I am %d years old'%(18))
#
# print("his height is %f m"%(1.70))
# print("his height is %.2f m"%(1.70))


# name = 'while'
# print(name[1:3])

#
# str_test = 'hello world'
#
# print(str_test[0:7])
# print(str_test[:7])
# print(str_test[2:])
# print(str_test[:])
# print(str_test[::2])
# print(str_test[::-1])
# print(str_test[1:9:-1])
# print(str_test[9:1:-1])
# print(str_test[9:1:-2])

# print(str_test[0:7:11])


str_test = 'hello world,'

print(str_test.count('l'))
print(str_test.count('o'))
print(str_test.find('world'))
print(str_test.rfind('world'))
print(str_test.rindex('o'))


