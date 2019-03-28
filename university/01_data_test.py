# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 10:59
# @Author  : for 
# @File    : 01_data_test.py
# @Software: PyCharm
import pymongo
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

client = pymongo.MongoClient("localhost",27017)
schools = client["sun"]
collection = schools["university"]

df = DataFrame(list(collection.find()))


df = df[df["code"]!=""]
# 汇总本科和专业
df.groupby(["subject"]).size()

