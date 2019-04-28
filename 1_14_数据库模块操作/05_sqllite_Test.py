#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 22:24
# @Author  : Xuegod Teacher For
# @File    : 05_sqllite_Test.py
# @Software: PyCharm
import peewee
db = peewee.SqliteDatabase('sql.db')
class Teacher(peewee.Model):
    name = peewee.CharField(max_length=20,default='for')
    age = peewee.IntegerField(default=18)
    class Meta:
        database = db
if __name__ == '__main__':
    # Teacher.create_table()
    s = Teacher('for','12')
    s.save()