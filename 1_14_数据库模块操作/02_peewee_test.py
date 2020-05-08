#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 22:02
# @Author  : Xuegod Teacher For
# @File    : 02_peewee_test.py
# @Software: PyCharm
import peewee

connect = peewee.MySQLDatabase(
    database='test',
    host = '127.0.0.1',
    user = 'root',
    passwd = '123456'
)

class Teacher(peewee.Model):

    name = peewee.CharField(max_length=20,default='for')

    age = peewee.IntegerField(default=18)

    class Meta:

        database = connect

if __name__ == '__main__':

    # Teacher.create_table()

    # Teacher.create(name='for',age = 18).save()
    #
    # Teacher.insert(name = 'kiss',age=49).execute()
    #
    # Teacher.update(name = 'kiss').where(Teacher.id == 1).execute()
    pass
    # 了解下加记忆，django时候