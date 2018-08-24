# -*- coding:utf-8 -*-
'''
银行卡类：
  属性：卡号、密码、余额、状态（是否锁定）

'''

class Card(object):

    def __init__(self, cardId, passwd, money,status):
        self.card_id = cardId
        self.passwd = passwd
        self.money = money
        self.status = status