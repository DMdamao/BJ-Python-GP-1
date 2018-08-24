#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 填写本模块功能大致描述
@Time    : 2018/8/11 上午10:34
@Author  : 北冥神君
@File    : 魔术方法研究.py
@Software: PyCharm
"""
'''
__名字__这样形式的就是魔术方法
'''

# 举例 __add__， 用类实现两个点坐标的和

class Rectangle(object):

    def __init__(self, length, width):
        """
        :param length:
        :param width:
        """
        self.lenght = length
        self.width = width

    def __add__(self, other):  # ‘+’号运算会触发该魔法方法，object1 + object2
        return self.lenght + other.lenght, self.width + other.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
print(rec1 + rec2)

print(rec1.__add__(rec2))  # 该结果和和上面的结果一样

'''
本质为执行了如下方法
rec1.__add__(rec2)

'''

# 举例 __radd__， 用类实现两个点坐标的和,右加


class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    # ‘+’号运算不会触发该魔法方法，因为+号默认是__add__要用此方法必须是调用__radd__方法，object1__radd__(object1)
    def __add__(self, other):
        return self.lenght + other.lenght, self.width + other.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
# print(rec1 + rec2)  不存在该方法，因为 ‘+ ’是__add__所有

print(rec1.__add__(rec2))  # 该结果和和上面的结果一样

'''
本质为执行了如下方法
rec1.__add__(rec2)

'''

# 举例 __sub__， 用类实现两个点坐标的差


class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __sub__(self, other):  # ‘-’号运算会触发该魔法方法，object1 - object2
        return self.lenght - other.lenght, self.width - other.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
print(rec1 - rec2)

print(rec1.__sub__(rec2))  # 该结果和和上面的结果一样

'''
本质为执行了如下方法
rec1.__sub__(rec2)

'''
# 举例 __rsub__， 用类实现两个点坐标的差,右减                


class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __rsub__(self, other):  # ‘-’号运算会触发该魔法方法，object2 - object1
        return other.lenght - self.lenght, other.width - self.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
# print(rec1 - rec2)  因为-号默认是用sub处理的。。所以要用必须用object1.__rsub__(object2)

print(rec2.__rsub__(rec1))  # 该结果和和上面的结果一样

'''
本质为执行了如下方法
rec1.__rsub__(rec2)

'''


# 举例 __mul__， 用类实现两个点坐标的乘积

class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __mul__(self, other):  # ‘*’号运算会触发该魔法方法，object1 * object2
        return self.lenght * other.lenght, self.width * other.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
print(rec1 * rec2)

print(rec1.__mul__(rec2))  # 该结果和和上面的结果一样

'''
本质为执行了如下方法
rec1.__mul__(rec2)

'''


# 举例 __mod_， 用类实现两个点坐标的取余数

class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __mod__(self, other):  # ‘%’号运算会触发该魔法方法，object1 % object2
        return self.lenght % other.lenght, self.width % other.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
print(rec1 % rec2)

print(rec1.__mod__(rec2))  # 该结果和和上面的结果一样

'''
本质为执行了如下方法
rec1.__mul__(rec2)

'''


# 举例 __iadd__， 用类实现两个点坐标的+号的自反运算符

class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __iadd__(self, other):  # ‘+=’号运算会触发该魔法方法，object1 += object2
        self.lenght = self.lenght + other.lenght
        self.width = self.width + other.width
        return self.lenght, self.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
rec1 += rec2
print(rec1)
# print(rec1.__iadd__(rec2))  # 该结果和和上面的结果一样 因为元素没有这个方法 故只能用 += 来实现。。。
'''
注意，元组没有__iadd__这个方法。只能用 +=来运算
rec1.__iadd__(rec2)

'''


# 举例 __isub__， 用类实现两个点坐标的-号的自反运算符

class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __isub__(self, other):  # ‘-=’号运算会触发该魔法方法，object1 += object2
        self.lenght = self.lenght - other.lenght
        self.width = self.width - other.width
        return self.lenght, self.width


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
rec1 -= rec2
print(rec1)
# print(rec1.__iadd__(rec2))  # 该结果和和上面的结果一样 因为元素没有这个方法 故只能用 -= 来实现。。。
'''
注意，元组没有__isub__这个方法。只能用 +=来运算
rec1.__isub__(rec2)

'''


# 举例 __imul__， 用类实现两个点坐标的*号的自反运算符

class Rectangle(object):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __imul__(self, other):  # ‘*=’号运算会触发该魔法方法，object1 *= object2
        self.lenght = self.lenght * other.lenght
        self.width = self.width * other.width
        return self.lenght, self.width


rec1 = Rectangle(3, 4)
rec2 = Rectangle(2, 2)
rec1 *= rec2
print(rec1)
# print(rec1.__iadd__(rec2))  # 该结果和和上面的结果一样 因为元素没有这个方法 故只能用 *= 来实现。。。
'''
注意，元组没有__isub__这个方法。只能用 +=来运算
rec1.__isub__(rec2)

'''


# 举例 __imod__， 用类实现两个数的*号的自反运算符

class Rectangle(object):
    def __init__(self, number):
        self.number = number

    def __imod__(self, other):  # ‘%=’号运算会触发该魔法方法，object1 %= object2
        self.number = self.number % other.number
        return self.number


rec1 = Rectangle(3)
rec2 = Rectangle(2)
rec1 %= rec2
print(rec1)
# print(rec1.__imod__(rec2))  # 该结果和和上面的结果一样 因为元素没有这个方法 故只能用 *= 来实现。。。
'''
注意，元组没有__isub__这个方法。只能用 +=来运算
rec1.__isub__(rec2)

'''
from os.path import join


class FileObject(object):

    def __init__(self, filepath='', filename='sample.txt'):
        self.file = open(join(filepath, filename), 'w')

    def __del__(self):
        print('关闭文件')
        self.file.close()
        del self.file


FileObject()


# 用魔术方法实现haskell语句的一个数据结构

class FunctionalList:
    def __init__(self, values):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        return self.values[0]

    def tail(self):
        return self.values[1:]

    def init(self):
        return self.values[:-1]

    def last(self):
        return self.values[-1]

    def drop(self, n):
        return self.values[n:]

    def take(self, n):
        return self.values[:n]


res = FunctionalList([1, 2, 3, 4, 5])

print(len(res))
print(res[1])
res[1] = 55
print(res[1])
del res[1]
print(res[1])
# res = iter(res)
# next(res)
# next(res)


# 描述器，单位转换

class Meter(object):
    def __init__(self, value=0.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Disctance(object):
    meter = Meter(10)
    foot = Foot()


d = Disctance()
print(d.foot, d.meter)