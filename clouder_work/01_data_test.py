# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 13:50
# @Author  : for 
# @File    : 01_data_test.py
# @Software: PyCharm
import pymongo
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 连接数据库
client = pymongo.MongoClient("localhost",27017)
cloud = client["sun"]
collection = cloud["clouderwork"]

data = DataFrame(list(collection.find()))

# periods = data.groupby(['period']).size()
#
# x = periods.index
# y = periods.values
# plt.figure()
# plt.scatter(x,y, color="#03a9f4", alpha = 0.5) # 绘制图表
# plt.xlim((0, 360))
# plt.ylim((0, 200))
# plt.xlabel("工期")
# plt.ylabel("项目数")
# plt.show()


# periods = data.groupby(["period"]).size().reset_index(name="count")
#
# df = periods[periods["period"]<=40]
#
# x = df["period"]
# y = df["count"]
#
# plt.figure()
# plt.scatter(x,y,label='项目数折线',color="#ff44cc")
# plt.title("工期对应项目数")
# plt.xlim((0, 360))
# plt.ylim((0, 500))
# plt.show()
#

periods = data.groupby(["period"]).size()

data = data[data["period"]==1][["name","period"]]
print(data)