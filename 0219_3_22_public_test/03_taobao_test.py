# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 10:55
# @Author  : for 
# @File    : 03_taobao_test.py
# @Software: PyCharm
import  time

a = ['while','for','django']

def outer(func):
    def inner(name):
        func(name)
        print('开始判断你有没哟登录')
        time.sleep(2)
        if name in a:
            print('已经登录成功，请敬请访问')
            time.sleep(1)
        else:
            print('你没有登录,没哟访问权限')
            time.sleep(1)
    return inner
@outer
def login(name):
    print('%s 要浏览'%name)
if __name__ == '__main__':
    login('fr')