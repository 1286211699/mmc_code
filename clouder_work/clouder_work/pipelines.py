# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
DATABASE_IP = '127.0.0.1'#指定ip
DATABASE_PORT = 27017#指定端口
DATABASE_NAME = 'sun'#指定数据库
client = pymongo.MongoClient(DATABASE_IP,DATABASE_PORT)#连接
db = client.sun#连接数据库
collection = db.clouderwork#生成表


class ClouderWorkPipeline(object):
    def process_item(self, item, spider):
        try:
            collection.insert(item)
        except Exception as e:
            print(e)
