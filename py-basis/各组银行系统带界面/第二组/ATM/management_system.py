#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
program name :
last modification time :
changelog :
"""


class Person(object):
    def __init__(self, record_file_id, name, id_card, age, sex, native_place, address):
        self.name = ""
        self.id_card = 0
        self.age = 0
        pass
    pass


class Card(object):
    def __init__(self, person, password, time):
        self.user = person
        self.password = password
        self.creating_time = time
        self.__card_id = 0
        self.__balance = 0
        pass
    pass


class Bank(object):
    pass
