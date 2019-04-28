#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 22:06
# @Author  : Xuegod Teacher For
# @File    : 04_peewee_test.py
# @Software: PyCharm
import peewee,datetime

connect = peewee.MySQLDatabase(
    database='news_test',
    host = '127.0.0.1',
    user = 'root',
    passwd = '123456'
)

class School(peewee.Model):
    name = peewee.CharField(max_length=20,default='for')
    address = peewee.CharField(max_length=30,default='xuegod')
    age = peewee.IntegerField(default=18)
    birthday = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = connect

if __name__ == '__main__':
    pass
    # School.create_table()
    #插入数据
    # s = School.create(name = 'for',age =12,birthday = '2017-10-10')
    # s.save()
    # School.insert(name = '小龙女',age = 18,birthday = '2018-6-12').execute()

    #更新
    # School.update(name = '杨过',age = 18).where(School.id == 1).execute()

    #删除
    # s = School.get(name = '杨过')
    # s.delete_instance()
    # School.delete_by_id(2)
    # School.delete().where(School.id == 2).execute()
    #查询
    # s = School.select()
    # for i in s:
    #     print(i.name,i.age)

    # s = School.get(School.id == 2)
    # print(s.name,s.age)

    # s = School.select().where(School.id == 3)
    # # print(s)
    # for i in s:
    #     print(i.name,i.age)
    #正序倒序查询
    # School.select().order_by(School.id.asc())
    # School.select().order_by(School.id.desc())