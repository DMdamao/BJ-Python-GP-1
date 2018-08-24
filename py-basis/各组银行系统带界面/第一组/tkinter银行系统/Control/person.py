# -*- coding:utf-8 -*-

'''
定义用户类
  属性：姓名、身份证号、电话号码

'''

class Person(object):
    def __init__(self, name, Idcard, tel):
        self.name = name
        self.Idcard = Idcard
        self.tel = tel
