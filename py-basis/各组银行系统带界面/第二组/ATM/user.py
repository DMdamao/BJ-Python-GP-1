#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
人
类名：Person
属性：姓名   身份证     电话号     卡号
行为：开户   查询  取款  存款  转账  改密  锁定  解锁  补卡  销户  退出
"""


class User(object):
    def __init__(self, record_file_id: str,
                 name: str,
                 card_number: int,
                 id_number: str,
                 address: str,
                 phone_number: int):
        self.record_file_id = record_file_id
        self.name = name
        self.card_number = card_number
        self.id_number = id_number
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return "<档案号：%s，名字：%s，身份证号：%s，卡号：%d，住址：%s,联系电话：%d>" % \
               (self.record_file_id, self.name, self.id_number, self.card_number, self.address, self.phone_number)

    pass


if __name__ == '__main__':
    per = User("123", "sad", 123, "1", "2", 134)
    print(per)
