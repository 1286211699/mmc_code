#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 21:24
# @Author  : Xuegod Teacher For
# @File    : 03_udp_client_test.py
# @Software: PyCharm
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('127.0.0.1',8001))

sock.sendto('client'.encode(),('127.0.0.1',9099))

data,address = sock.recvfrom(521)

print(data.decode(),address)

sock.close()