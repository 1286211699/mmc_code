#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:57
# @Author  : Xuegod Teacher For
# @File    : 04_seek_test.py
# @Software: PyCharm
# f = open('1.txt','r+',encoding='utf-8')
#
# print(f.name)
#
# print(f.readline())
# f.seek(0,0)
# print(f.readline())
#
# pos = f.tell()
# print('当前的指针位置：%s'%pos)
#
# f.close()




import time

def reader(path,line = 3):

    with open(path,'r',encoding='utf-8') as f:
        #吧指针指向文件的末尾
        f.seek(0,2)
        #告诉我整个文件有多少个字节
        end = f.tell()
        #指针指向文件开头
        f.seek(0,0)
        #询问是否开启自动
        auto = input('你要开启自动吗(y/n)?')
        #如果符合条件
        if auto == 'y':
            #死循环
            while True:
                #每次读取三行
                for i in range(line):
                    print(f.readline())
                time.sleep(2)#两秒
                #如果你只针对位置和和最后的字节数相同
                if f.tell() == end:
                    break
        else:
            con = 'N'
            f.seek(0,2)
            end = f.tell()
            f.seek(0,0)
            while True:

                if con == 'N':
                    for i in range(line):
                        print(f.readline())
                else:
                    print('请输入N:')
                if f.tell() == end:
                    break

                con = input('>>>')


if __name__ == '__main__':
    reader('1.txt')










