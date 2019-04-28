#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 10:29
# @Author  : Xuegod Teacher For
# @File    : 01_KNN_相邻算法.py
# @Software: PyCh
import numpy as np
import operator

def createDataSet():
    #四组二维特征
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    #四组特征标签
    labels = ['爱情片','爱情片','动作片','动作片']
    return group,labels
def classify0(inX,dataSet,labels,k):#dataSet == group inX == test==[101,20]
    #numpy函数中的shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    #tile矩阵重复，datasetsize为4所以行重复四次[[101,20],[101,20],[101,20],[101,20]]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    #二维特征相减后的平方
    sqDiffMat = diffMat ** 2
    print(sqDiffMat)
    #以一行进行加和，返回的数据为一个列表
    sqDistances = sqDiffMat.sum(axis=1)
    #开方，计算出距离
    distances = sqDistances ** 0.5
    #返回distances中的元素大小，从小到大进行排序后的索引值
    sortedDistIndices = distances.argsort()#[2,3,1,0]
    #定义一个记录类别次数的字典
    classCount = {}

    for i in range(k):#k为3
        voteIlabel = labels[sortedDistIndices[i]]
        #计算出类别的次数
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    #降序排序字典返回一个[('动作片', 2), ('爱情片', 1)]
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True)
    #返回次数最多的类别
    print(sortedClassCount)
    return sortedClassCount[0][0]

if __name__ == '__main__':

    group,labels = createDataSet()
    print(group)
    print(labels)
    print('---------------')
    test = [101,20]
    test_class = classify0(test,group,labels,3)
    print(test_class)
