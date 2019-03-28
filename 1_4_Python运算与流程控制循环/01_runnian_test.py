# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 15:03
# @Author  : for 
# @File    : 01_runnian_test.py
# @Software: PyCharm
year = int(input('请输入一个年份:'))
# 普通年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）；
# 世纪年:能被400整除的为世纪闰年。（如2000年是闰年，1900年不是闰年）；
if year % 4 ==0 and year % 100 != 0 or year %400 == 0:
    print('{}是闰年'.format(year))
else:
    print('{}不是闰年'.format(year))
