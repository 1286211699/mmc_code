#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 21:19
# @Author  : Xuegod Teacher For
# @File    : 02_pymysql_test.py
# @Software: PyCharm
#删除
import pymysql
db = pymysql.connect('localhost','root','123456','news_test',charset = 'utf8')
cursor = db.cursor()
sql = "update test_sql set name = 'django' where id =2 "

# name = input('请输入你的姓名:')
# age = input('请输入你的年龄:')
cursor.execute(sql)
db.commit()
cursor.close()
db.close()