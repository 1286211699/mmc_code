#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 21:12
# @Author  : Xuegod Teacher For
# @File    : 03_re_test.py
# @Software: PyCharm
import re
#\d代表的是数字范围 \D
#\w [A-Za-z0-9]
#\W [A-Za-z0-9]
#* 代表重复前一个字符的0-无限次
#+代表重复前一个字符的1-无限次


text = '''
<thead>
    <tr>
      <th class = 'ok'>Month</th>
      <th>Savings</th>
    </tr>
  </thead>
'''


# data = re.findall(r'\w+$',text,re.M)
data = re.findall(r'<tr>.*?</th>',text,re.S)

print(data)

