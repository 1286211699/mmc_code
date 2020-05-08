#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 21:52
# @Author  : Xuegod Teacher For
# @File    : 08_magic_test.py
# @Software: PyCharm
'''
10.6.1  __del__()方法
创建对象后，python解释器默认调用__init__()方法；
当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法
当内存中构建一个对象数据的时候回调__init__()方法，
当内存中销毁（释放）一个对象时回调__del__()方法。

'''

# class Hero:
#     def __init__(self):
#         print('init')
#
#     def __del__(self):
#         print('del')
#
# man1 = man = Hero()
# del man
# del man1
# print('程序结束')
'''
10.6.2  __new__()方法
__new__至少要有一个参数cls，代表要实例化的类(并不是对象)，此参数在实例化时由Python解释器自动提供。
__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return object的__new__出来的实例。
__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值。
我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节。
简单来说__new__方法，就是创建一个实例。
new一个对象
new和init 那个执行顺序优先
'''

class Hero:
    def __init__(self,name,age):
        print('__init__')

    def __new__(cls, a,b):
        print('new')
        return  object.__new__(cls)


a = Hero('for',18)

'''
10.6.3  __str__()方法
__str__：在将对象转换成字符串str(对象)的时候，打印对象的信息。
__str__方法必须要return一个字符串类型的返回值，作为对实例对象的字符串描述。
__str__实际上是被print函数默认调用的，当要print（实例对象）时，默认调用__str__方法，将其字符串描述返回。
当你打印一个类的时候，那么print首先调用的就是类里面的定义的__str__。
str()
'''
# class Hero:
#
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return 'my name is %s'%self.name
#
#     # def __call__(self, *args, **kwargs):
#
# t = Hero('for')
# #print这个方法会自动调用str魔法方法
# print(t)
#



