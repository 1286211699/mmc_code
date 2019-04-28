#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 11:34
# @Author  : Xuegod Teacher For
# @File    : 02_海伦择偶_test.py
# @Software: PyCharm
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines

def file2matrix(filename):

    with open(filename) as fr:
        #读取所有以列表进行返回
        arrayOLines = fr.readlines()
        #总共的数据 的长度
        numberOfLines = len(arrayOLines)
        #发挥numpy矩阵，解析完成数据，numberOflines行 3列
        returnMat = np.zeros((numberOfLines,3))
        print('return',returnMat)
        #返回分类标签向量
        classLabelVector = []
        #行的索引值
        index = 0

        for line in arrayOLines:

            line = line.strip()

            listFromLine = line.split('\t')

            returnMat[index,:] = listFromLine[0:3]

            if listFromLine[-1] == 'smallDoses':

                classLabelVector.append(1)

            elif listFromLine[-1] == 'largeDoses':

                classLabelVector.append(2)
            else:
                classLabelVector.append(3)
            index += 1
        return returnMat,classLabelVector
if __name__ == '__main__':

    filename = 'datingTestSet.txt'

    daringDataMat,datingLabels = file2matrix(filename)

    print(daringDataMat,datingLabels)

