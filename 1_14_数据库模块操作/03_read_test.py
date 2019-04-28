#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 21:49
# @Author  : Xuegod Teacher For
# @File    : 03_read_test.py
# @Software: PyCharm

import pymysql

db = pymysql.connect('localhost','root','123456','news_test',charset = 'utf8')

cursor = db.cursor()

cursor.execute('select * from test_sql')

data = cursor.fetchone()
print(data)
data = cursor.fetchall()
print(data)

cursor.close()
db.close()
