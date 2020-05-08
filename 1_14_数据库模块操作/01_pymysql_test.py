#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 21:11
# @Author  : Xuegod Teacher For
# @File    : 01_pymysql_test.py
# @Software: PyCharm

import pymysql
# class MysqlTest:
#     def __init__(self,da):
#         pass
#     # def delete(self,id):
#charset ？test是啥？
db = pymysql.connect('localhost','root','123456','test',charset = 'utf8')
#相当于一个操作者
cursor = db.cursor()
#创建表，很简单
# sql = '''create table test_sql(
# id int PRIMARY key auto_increment,
# name varchar (30),
# age INT
# )
# '''
#在表中增添一部分数据，灵动添加，爬虫
# sql = '''insert into test_sql(name,age) value (%s,%s)'''
#删除
# sql = '''delete from test_sql where id = 1'''
#修改数值
# sql = '''update test_sql set name = '龙女' where id = 3'''
'''
fetchone() 这个方法获取一个，类似于咱们的readline
fetchall()  这个方法是返回所有的结果
'''

#执行sql语句
cursor.execute("select * from test_sql")
#fetchone
# print(cursor.fetchone())
# print(cursor.fetchone())
#fetchall
# print(cursor.fetchall())
# fetchmany()
# print(cursor.fetchmany(2))

#提交给数据库，主要是配合增加修改删除操作
# db.commit()

cursor.close()

db.close()

'''
class test(object):
    def __init__(self):
        pass
    def delete_by_id(self,id):
        pass
    def insert_data(self,name):
        pass
    def update_data(self,name):
        pass
    def __del__(self):
        db.close()
'''

