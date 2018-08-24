# -*- coding:utf-8 -*-
from bank import Bank
from atm import ATM
from atminitview import View
import os
import pickle

#创建银行对象

atmMachine = ATM()
view = View()
atmMachine.money = 10000
fipath = os.path.join(os.getcwd(), "alluser.txt")
f = open(fipath, "rb")
allusers = pickle.load(f)
Bank().usersDict = allusers
def main():
    # 展示开机界面
    while True:
        view.welcome()
        optionStr = view.adminview()
        if optionStr == "11":
            res = atmMachine.checkPasswd()
            if not res:
                # 循环进入欢迎界面
                welcome()
        elif optionStr == "22":
            f = open(fipath, "wb")
            pickle.dump(Bank().usersDict, f)
            f.close()
            break
        elif optionStr == "33":
            atmMachine.addMoney()
        elif optionStr == "44":
            atmMachine.changeAtmPasswd()

def welcome():
    while True:
        # 接收操作
        optionStr = view.userview()
        # 匹配操作
        if optionStr == "111":
            # 循环进入操作界面
            res = atmMachine.checkCard()
            if res:
                option(res[0], res[1])
        elif optionStr == "222":
            atmMachine.createCard()
        elif optionStr == "333":
            atmMachine.new_card()
        elif optionStr == "444":
            view.error("返回开机界面……")
            break

def option(user, card):
    while True:
        # 接收操作
        optionStr = view.optionsView()
        # 匹配操作
        if optionStr == "1":
            atmMachine.searchCard(card)
        elif optionStr == "2":
            atmMachine.transfer_accounts(card)
        elif optionStr == "3":
            atmMachine.deposit(card)
        elif optionStr == "4":
            atmMachine.withdrawal(card)
        elif optionStr == "5":
            if atmMachine.change_password(card) == 0:
                break
            else:
                continue
        elif optionStr == "6":
            if atmMachine.logout(user, card) == 0:
                break
            else:
                continue
        elif optionStr == "7":
            atmMachine.lock(user, card)
        elif optionStr == "8":
            atmMachine.unlock(user, card)
        elif optionStr == "9":
            break

if __name__ == "__main__":
    main()




