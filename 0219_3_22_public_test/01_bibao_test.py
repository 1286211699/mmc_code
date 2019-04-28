# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 10:07
# @Author  : for 
# @File    : 01_bibao_test.py
# @Software: PyCharm
# def outer():
#     # a = 1
#     def inner():
#         # print(a)
#         print('I am inner')
#     return inner
# if __name__ == '__main__':
#     a = outer()
#     print(a)
#     a()



def outer(num):
    def inner(num_in):
        # print(a)
        print('inner num_in is %d'%num_in)
        return num_in+num
    return inner
if __name__ == '__main__':
    a = outer(20) #a == inner()
    print(a)
    print(a(200))# inner(200)










