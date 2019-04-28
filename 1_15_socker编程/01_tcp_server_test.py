#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 21:02
# @Author  : Xuegod Teacher For
# @File    : 01_tcp_server_test.py
# @Software: PyCharm
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('',9000))

sock.listen(5)

content,address = sock.accept()
print('%s:%s is connected'%address)

content.send('hello'.encode())

print(content.recv(521).decode())

sock.close()


