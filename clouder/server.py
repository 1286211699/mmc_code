#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 13:59
# @Author  : Xuegod Teacher For
# @File    : server.py
# @Software: PyCharm
import socket
import json
import sys
from urllib import request
def computer(info):
    key='2fc58f256e8c4e1bba723fe2c976b614'
    api='http://www.tuling123.com/openapi/api?key='+key+'&info='+info
    response=request.urlopen(api).read()
    client_json=json.loads(response)
    return 'computer:'+client_json['text']
s=socket.socket()
host=socket.gethostname()
port=3456
s.bind((host,port))
s.listen(5)
while True:
    clnt,add=s.accept()
    print("clnt's add is:",add)
    data=clnt.recv(1024)
    print(data.decode())
    result=computer(data.decode())
    clnt.send(result.encode())
s.close()

