#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 21:01
# @Author  : Xuegod Teacher For
# @File    : 02_赋值_test.py
# @Software: PyCharm

#传统赋值
# name = 'for'

#链式赋值
# name = user = 'for'
# print(id(name))
# print(id(user))
#序列解包赋值
# name,age = 'for',18
# print(name,age)

# 现在不使用第三个变量的情况下，a = 2 ,b  =1
#python 前几年 16 python
# a = 1
# b = 2
# a,b = b,a
#
# print(a)


#ctrl + 鼠标左键
# print('大家晚上好')


# print('''
#      へ　　　　　／|
# 　　/＼7　　　 ∠＿/
# 　 /　│　　 ／　／
# 　│　Z ＿,＜　／　　 /`ヽ
# 　│　　　　　ヽ　　 /　　〉
# 　 Y　　　　　`　 /　　/
# 　ｲ●　､　●　　⊂⊃〈　　/
# 　()　 へ　　　　|　＼〈
# 　　>ｰ ､_　 ィ　 │ ／／
# 　 / へ　　 /　ﾉ＜| ＼＼
# 　 ヽ_ﾉ　　(_／　 │／／
# 　　7　　　　　　　|／
# 　　＞―r￣￣`ｰ―＿
#     ''')
#
#input讲解
# name = input('请输入你的姓名:')
#
# print(name)
# print(type(name))



#字符串讲解
# a = '1'
# b = "name's for"
# print(a+b)
# print(b)
# print(type(b))

# print(type(3/2)) #浮点型
# print(type(3//2)) #int
#
#
# #字符串占位符
# print('my name is %s'%('for'))
# print('my age is %d'%(18))
# print('my height is %f'%(1.78))
# print('my height is %.2f'%(1.78))




# name = 'while'

# print(name[0])
# print(name[2])
# print(name[4])
# print(name[5])

# print(name[1:3])


str_test = 'hello world'

# print(str_test[0:7])
print(str_test[::-1])

print(str_test[1:3:-1])

print(str_test[3:1:-1])


# print(str_test[0:7:3]) #3-1 = 2

