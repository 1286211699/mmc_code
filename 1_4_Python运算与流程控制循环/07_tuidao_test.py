# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 16:39
# @Author  : for 
# @File    : 07_tuidao_test.py
# @Software: PyCharm
#列表推导式
# 比如现在我们要生成一个列表，列表当中的元素为0-10，首先我们不用列表推导式，该如何来实现？


# result = [i for i in range(10) if i % 2 == 0]
# print(result)
#
# result = []
# for i in range(10):
#     if i % 2 == 0:
# #         result.append(i)
# # print(result)
#
# # 那么问题来了，比如现在有一列表L = [[1,2,3],[4,5,6],[7,8,9]]
# # 要求出1/4/7  和 1/5/9 元素，思考如何取出？
# L = [[1,2,3],[4,5,6],[7,8,9]]
# #取到 147
# result = [L[0] for i in L]
# #159
# result1 = [L[i][i] for i in range(len(L))]
#
# print(result)
#
# print(result1)
#
#
# # 2个for循环
#
# a = [(i,j) for i in range(1,5) for j in range(6,10)]
# print(a)
#
# for i in range(1,5):
#     for j in range(6,10):
#         pass
#
# a = [(x,y,z) for x in range(2)for y in range(2)for z in range(2)]
# print(a)


# 4.3.2  字典推导式
# 字典和集合推导式是该思想的延续，语法差不多，只不过产生的是集合和字典而已。

# dic2 = {k:v for k,v in {'name':'for','age':18}.items()}
# print(dic2)


# 4.3.3  集合推导式
# 集合推导式跟列表推导式非常相似，唯一区别在于用{}代替[]

# L = [1,2,3,1,2,3,4]
#
# set1 = {i for i in L}
#
# print(set1)



# 4.3.4  元组生成式

a = (i for i in range(5))

for i in a:
    print(i)