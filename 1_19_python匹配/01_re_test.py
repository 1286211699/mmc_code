#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 20:45
# @Author  : Xuegod Teacher For
# @File    : 01_re_test.py
# @Software: PyCharm

# print('I am \nfor')
# print(r'I am \nfor')
import re
# . 代表任意字符 a-z A-Z 0-9 ^ *%
# \ 去除正则表达式特殊语义
# data = re.findall(r'a\.c','a.c')
#字符集：[abc]  如果要匹配 我们只能匹配一个 a 或b或 c
# data = re.findall(r'a[abc]c','aac')
# data = re.findall(r'a[0-9]c','a2c')
#疑惑：如果我想精确的匹配？
'''
\d :匹配数字的字符[0-9]
\D :匹配非数字的字符（包含了特殊字符）
'''
# data = re.findall(r'a\dc','aAc')
# data = re.findall(r'a\Dc','a c')
'''
\s :匹配空字符串，或者是\n \t \f \v
\S :匹配非空字符串 
'''
# data = re.findall(r'a\sc','a\nc')
# data = re.findall(r'a\Sc','abcacc')

'''
\w: 匹配单词字符[A-Za-z0-9](不能匹配特殊字符)
\W: 匹配非单词字符
'''
# data = re.findall(r'a\wc','abca*c')
# data = re.findall(r'a\Wc','abca*c')

'''
*: 匹配前一个字符的0 次或无限多次 : 我大for .* exceptions
+: 匹配前一个字符的1 次或无限多次
{m} :匹配前一个字符m次
{m,n}:匹配前一个字符的m~n次
'''
# data = re.findall(r'abc*','ab')
# data = re.findall(r'abc+','abcc')
# data = re.findall(r'abc{1,3}','abccc')

'''
^ : 匹配字符串开头，django开发中的url地址中使用
$ : 匹配字符串结尾, django开发中的url地址中使用
\A :匹配字符串开头
\Z:匹配字符串结尾
\b：单词边界，单词和符号之间的边界
'''
# data = re.findall(r'^abc{1,3}','abccc')
# data = re.findall(r'^a\w+c$','abccc')

'''
上边所讲解的范围的匹配，只是具体的一个字符+
| :左边有个表达式，右边也有表达式，总是先尝试匹配左边的，一但成功就直接逃过右边的表达式
如果我在配合():想比着普通的匹配（）内的优先级更高
'''
# data = re.findall(r'a\wc|def','abcdef')
# data = re.findall(r'a(?:\wc|de)c','abccadec')
#这个时候，我就静下来想想？(.*) 在爬虫的时候
# data = re.findall(r'(abc){2}','abcabc')


# print(data)

'''
匹配手机号？ 11位
18737310111 
第一位固定的 1 灵活就看各位了
1(3\w|6\w|8[0-9])[0-9]{8}
(?:+861|1)(?:3\w|6\w|8[0-9])[0-9]{8}
'''

# data = re.findall(r'1(?:3\w|6\w|8[0-9])[0-9]{8}','18737310111,18737310119')
# print(data)
'''
匹配邮箱
abcdef@qq.com
abcdef@163.com
\w+@\w+\.\w+m
[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+m
.*\..*m
.*
我写这些匹配规则了吗？
'''


'''
30 讲课了，我认为来的人很少，五月一日了，我带咱们班 10 白讲
4,5 会加班的，问下我关于问题?
主业：数学老师 教师资格证的 叫高中

'''












