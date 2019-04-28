
numbers = [10086, 10000, 10010, 9558]
names = ['中国移动', '中国电信', '中国联通']

def myzip(iter1, iter2):
    it1=iter(iter1)  # 拿出一个迭代器
    it2=iter(iter2)
    while True:
        a=next(it1)
        b=next(it2)
        yield (a, b)

for t in myzip(numbers, names):  # 能实现与zip同样的功能
    print(t)
