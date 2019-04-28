#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 21:55
# @Author  : Xuegod Teacher For
# @File    : client.py
# @Software: PyCharm
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('127.0.0.1',8005))

sock.send('client1'.encode())

print(sock.recv(521).decode())

sock.close()