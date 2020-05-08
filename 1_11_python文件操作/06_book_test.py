#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 22:00
# @Author  : Xuegod Teacher For
# @File    : 06_book_test.py
# @Software: PyCharm
'''
自动翻页
手动翻页
'''
import time
class Book:

    def read_book(self,path):

        with open(path,'r',encoding='utf-8') as f:

            #文件中的全部字节
            f.seek(0,2)

            end = f.tell()
            # print(end)

            f.seek(0,0)

            auto = input('是否开启自动功能？(y/n)')

            if auto == 'y':

                while True:
                    for i in range(3):
                        print(f.readline())
                    time.sleep(2)

                    if f.tell() == end:
                        break

            else:
                #
                con = 'N'

                while True:

                    if con == 'N':
                        for i in range(3):
                            print(f.readline())
                    else:
                        print('请输入N')
                    if f.tell() == end:
                        break

                    con = input('>>>')

if __name__ == '__main__':
    # read_book('1.txt')
    b = Book()
    b.read_book('1.txt')
