#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 21:05
# @Author  : Xuegod Teacher For
# @File    : 01_TCP_client_test.py
# @Software: PyCharm
import socket
#创建一个套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#链接服务器
sock.connect(('127.0.0.1',9000))
#给服务器接受数据
print(sock.recv(521).decode())
#发送数据
sock.send('client'.encode())
#关闭套接字
sock.close()


# print('adc'.encode())