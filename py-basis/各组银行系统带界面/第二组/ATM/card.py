#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hmac
from random import randrange
from bank import Bank
"""
卡
类名：Card
属性：卡号   密码  余额
行为
"""


class Card(object):
    card_id_list = {}
    bank = Bank()

    def __init__(self, passwd: int = None, card_number=None):
        if card_number is None:
            self.card_number = self.bank.get_empty_card_number()
            self.card_id_list[self.card_number] = self.hash(self.card_number, passwd)
            self.balance = 0
            self.state = "normal"  # "frozen"
            self.bank.register("card_data.txt",
                               card_number=self.card_number,
                               card_id=self.card_id_list[self.card_number],
                               balance=self.balance,
                               state=self.state)
        else:
            c, i = self.bank.find_card(card_number)
            self.card_number = c["card_number"]
            self.card_id_list[self.card_number] = c["card_id"]
            self.balance = c["balance"]
            self.state = c["state"]

    def change_password(self, new_password):
        self.card_id_list[self.card_number] = self.hash(self.card_number, new_password)
        pass

    # @property
    # def balance(self):
    #     return self.__balance
    #
    # @balance.setter
    # def balance(self, value):
    #     # 身份检查，防止用户自行修改卡上的余额
    #     self.__balance = value

    @staticmethod
    def hash(id_: int, password: int):
        h = hmac.new(str(password).encode("UTF-8"), str(id_).encode("UTF-8"), digestmod="SHA1")
        return h.hexdigest()

    pass


if __name__ == '__main__':
    card = Card(666666, 10000000)
    print(card.balance, card.balance)

