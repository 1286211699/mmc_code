#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 21:06
# @Author  : Xuegod Teacher For
# @File    : 01_pymysql_test.py
# @Software: PyCharm

import pymysql
#链接数据库，参数分为 本地地址，用户名，密码 ，数据库，字符集
db = pymysql.connect('localhost','root','123456','news_test',charset = 'utf8')
#是用cuosor这个方法创建一个游标对象，相当于一个操作者
cursor = db.cursor()
#编写sql语句
sql = '''insert into test_sql(name,age) value('for',18)'''
#执行sql语句
cursor.execute(sql)
#提交给数据库
db.commit()
#关闭游标
cursor.close()
#关闭数据库连接
db.close()

