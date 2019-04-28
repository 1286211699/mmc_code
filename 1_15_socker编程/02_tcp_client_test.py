#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 21:07
# @Author  : Xuegod Teacher For
# @File    : 02_tcp_client_test.py
# @Software: PyCharm
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('127.0.0.1',9000))

print(sock.recv(521).decode())

sock.send('Hi'.encode())

sock.close()