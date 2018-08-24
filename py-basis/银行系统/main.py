# -*- coding:utf-8 -*-
from bank import Bank
from atm import ATM
from user import User
from card import Card

import time
'''
人：User
属性：姓名  身份证号码  电话号   卡（多张卡  {卡号：卡对象,……} ）
行为：插卡   输入信息

卡：Card
属性：卡号   密码    余额     是否锁定
行为：

提款机：ATM
属性：系统账号   系统密码    余额     是否正常
行为：
    开机界面、欢迎界面、操作界面
    修改系统密码、提额
    开户、查询、存款、取款、转账、改密、锁定、解锁、注销、补卡、退出

银行（单例）：Bank
属性：用户字典({身份证号:用户对象, ……})
行为：
'''
#创建银行对象
BANK = Bank()
atmMachine = ATM()
atmMachine.money = 10000


def main():
    while True:
        #展示开机界面
        atmMachine.atmInitView()
        #接收操作
        optionStr = input("请输入操作:")
        #匹配操作
        if optionStr == "11":
            res = atmMachine.checkPasswd()
            if not res:
                # 循环进入欢迎界面
                time.sleep(2)
                welcome()
        elif optionStr == "22":
            atmMachine.shutDown()
            break
        elif optionStr == "33":
            atmMachine.addMoney()
        elif optionStr == "44":
            atmMachine.changeAtmPasswd()

        time.sleep(2)


def welcome():
    while True:
        atmMachine.welcomeView()
        # 接收操作
        optionStr = input("请输入操作:")
        # 匹配操作
        if optionStr == "111":
            # 循环进入操作界面
            res = atmMachine.checkCard()
            if res:
                time.sleep(2)
                option(res[0], res[1])
            time.sleep(2)
        elif optionStr == "222":
            atmMachine.createCard()
        elif optionStr == "333":
            atmMachine.reisse()
        elif optionStr == "444":
            print("返回开机界面……")
            break
        time.sleep(2)


def option(user, card):
    while True:
        atmMachine.optionsView(user.name, card.cardId)
        # 接收操作
        optionStr = input("请输入操作:")
        # 匹配操作
        if optionStr == "1":
            atmMachine.searchCard(card)
        elif optionStr == "2":
            atmMachine.transfer(card)
        elif optionStr == "3":
            atmMachine.deposit(card)
        elif optionStr == "4":
            atmMachine.withdrawal(card)
        elif optionStr == "5":
            ret = atmMachine.changepasswd(card)
            if not ret:
                break
        elif optionStr == "6":
            ret = atmMachine.logout(card)
            if not ret:
                break
        elif optionStr == "7":
            atmMachine.lock(user,card)

        elif optionStr == "8":
            atmMachine.unlock(user, card)
        elif optionStr == "9":
            break

        time.sleep(2)

if __name__ == "__main__":
    main()





