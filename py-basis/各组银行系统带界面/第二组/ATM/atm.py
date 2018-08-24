#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uuid
from interface import ATMGui
from card import Card
from bank import Bank
from user import User
"""
提款机
类名：ATM
属性：
行为：开户   查询  取款  存款  转账  改密  锁定  解锁  补卡  销户  退卡
open_count
check_balance
withdrawal
deposit
transfer_accounts
change_password
freeze_card
unfreeze_card
card_reissue
account_cancellation
refund_card
"""


class ATM(object):
    bank = Bank()

    def __init__(self):
        self.id = uuid.uuid1()
        self.gui = ATMGui(self.open_count,
                          self.withdrawal,
                          self.deposit,
                          self.transfer_accounts,
                          self.change_password,
                          self.freeze_card,
                          self.unfreeze_card,
                          self.card_reissue,
                          self.account_cancellation,
                          self.refund_card,
                          self.read_card,
                          self.login)
        self.card = None
        self.user = None

    def loop(self):
        self.gui.loop()

    def read_card(self, card_number: int=None):
        d = self.bank.find_card(card_number)
        if (card_number is None) or (d is None):
            self.gui.message_box("警告！", "卡不存在或卡号为空!")
        else:
            if d[0]["state"] != "frozen":
                self.card = Card(card_number=card_number)
                self.gui.page_login(card_number)
            else:
                self.gui.message_box("警告！", "卡被冻结，请解锁后再使用!")

    @staticmethod
    def id_number_check(id_number: str):
        if len(id_number) == 18:
            co = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            check = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
            sum = 0
            num = list(id_number)
            parity_bit = num.pop()
            for index, i in enumerate(num):
                sum += co[index] * eval(i)
            sum %= 11
            if parity_bit == check[sum]:
                return True
            else:
                return False

    def open_count(self, name: str, id_num: str, phone_number: str, address: str, password: int):
        if (password is not None) and (self.id_number_check(id_num)):
            # if self.bank.find_user(id_number=id_num) is not None:
            self.gui.message_box("恭喜！", "您已成功开户!")
            # 判断信息真伪
            self.card = Card(passwd=password)
            self.user = User(uuid.uuid1(), name, self.card.card_number, id_num, address, phone_number)
            self.gui.page_count(self.card.card_number, self.card.balance)
            # else:
            #     self.gui.message_box("警告！", "一张卡够多了!")
        else:
            self.gui.message_box("警告！", "信息有误!")

    def login(self, card_number, password):
        d, i = self.bank.find_card(card_number)
        if d["card_id"] == self.card.hash(self.card.card_number, password):
            self.gui.page_count(self.card.card_number, self.card.balance)

    def withdrawal(self, event, sum):
        if (self.card.balance - sum >= 0) and (sum >= 0):
            self.card.balance -= sum
            self.gui.page_count(self.card.card_number, self.card.balance)
        else:
            self.gui.message_box("警告！", "你没那么多钱，就别取那么多！")

    def deposit(self, sum):
        if sum >= 0:
            self.card.balance += sum
            self.gui.page_count(self.card.card_number, self.card.balance)
        else:
            self.gui.message_box("警告！", "点存钱就别取钱！")

    def transfer_accounts(self, card_id, sum):
        if (self.card.balance - sum >= 0) and (sum >= 0) and (self.bank.find_card(card_id) is not None):
            self.card.balance -= sum
            other_card, i = self.bank.find_card(card_id)
            other_card["balance"] += sum
            self.bank.update_card_data(card_id, other_card)
            self.gui.message_box("恭喜！", "转账成功！")
            self.gui.page_count(self.card.card_number, self.card.balance)
        else:
            self.gui.message_box("警告！", "账号不存在或金额不正确！")

    def change_password(self, old_password, new_password):
        if self.card.hash(self.card.card_number, old_password) == self.card.card_id_list[self.card.card_number]:
            self.card.card_id_list[str(self.card.card_number)] = self.card.hash(self.card.card_number, new_password)
            self.refund_card()
        else:
            self.gui.message_box("警告！", "这卡真的是你的吗？我吞了！")

    def freeze_card(self):
        self.card.state = "frozen"
        self.refund_card()

    def unfreeze_card(self, card_number):
        d, i = self.bank.find_card(card_number)
        d_new = dict()
        d_new["card_number"] = card_number
        d_new["card_id"] = d["card_id"]
        d_new["balance"] = d["balance"]
        d_new["state"] = "normal"
        self.bank.update_card_data(card_number, d_new)
        self.gui.page_home()

    def card_reissue(self, event):
        pass

    def account_cancellation(self):
        d = dict()
        d["card_number"] = 0
        d["card_id"] = "x"
        d["balance"] = 0
        d["state"] = "x"
        print(self.card.card_number)
        print("---")
        self.bank.update_card_data(self.card.card_number, d)
        self.card = None
        self.user = None
        self.gui.page_home()

    def refund_card(self):
        d = dict()
        d["card_number"] = self.card.card_number
        d["card_id"] = self.card.card_id_list[str(self.card.card_number)]
        d["balance"] = self.card.balance
        d["state"] = self.card.state
        self.bank.update_card_data(self.card.card_number, d)
        self.card = None
        self.user = None
        self.gui.page_home()


if __name__ == '__main__':
    atm = ATM()
    atm.loop()
