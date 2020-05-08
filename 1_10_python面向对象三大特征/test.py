class Dog(object):
    def print_self(self,name,age):
        print('Hello,I am dog')
        print(name,age)
    def __call__(self, *args, **kwargs):
        print('gagag')

# repr('a')
# print()
class Tom(Dog):
    pass
    # def print_self(self,name,age,num):
        #调用父类的方法
        # super().print_self(name,age)
        # print(num)
        # Dog.print_self(self)
#         # print('Hi I am tom')
T = Tom()
T('name')

# T.print_self('for',19,10)
# callable()