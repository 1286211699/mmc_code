#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 15:22
# @Author  : Xuegod Teacher For
# @File    : 02_xlwt_test.py
# @Software: PyCharm
import csv
import xlsxwriter
import xlwt

workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)

sheet = workbook.add_sheet('test',cell_overwrite_ok=True)

sheet.write(0,0,'name')
sheet.write(1,0,'project')
sheet.write(0,1,'while')
sheet.write(1,1,'for')
# sheet.write(0,0,'name')
workbook.save('xuegod.xls')