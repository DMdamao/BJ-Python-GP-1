# -*- coding:utf-8 -*-
from bank import Bank
from user import User
from card import Card

import random

import tkinter
class ATM(object):
    def __init__(self):
        # self.inputPasswd = inputPasswd()
        self.account = "1"
        self.passwd = "1"
        self.money = 0
        self.isActive = True

    def atmInitView(self):
        return """  
        登陆                                     关机
      
                       
        提额                                     改密                 
              """
    def welcomeView(self):
        return  """           Welcome to Tan bank      
                
       插卡                                     开户 
  
                
       补卡                                     返回                
        """

    def optionsView(self, name, cardId):

        return """           用户名:%s             卡号:%s  
               查询                                    转账   


               存款                                    取款   


               改密                                    注销       


               锁定                                    解锁         

                                  退卡      
               """ % (name, cardId)

    def checkPasswd(self,account,passwd):
        if account != self.account or passwd != self.passwd:

            return 1 , "账号或密码错误"
        else:
            return 0, "系统设置成功，正在启动……"
    #关机
    def shutDown(self):
        #数据持久化
        print("正在保存数据……")
    #提额
    def addMoney(self,money):
        self.money += money
        return "提额成功！！"
        if not self.isActive:
            self.isActive = True

    def changeAtmPasswd(self,passwd, passwd1, passwd2):
        if passwd != self.passwd:
            return "密码错误，修改失败"
        else:
            if passwd1 != passwd2:
                return "两次密码不同，修改失败"
            else:
                self.passwd = passwd1
                return "系统密码修改成功"
    #银行卡改密
    def changeCardPasswd(self,card,passwd, passwd1, passwd2):
        if card.isLock:
            return 0,"该卡已被锁定，请解锁后继续其他操作！"
        else:
            if passwd != card.passwd:
                return -1,"密码错误，修改失败"
            else:
                if passwd1 != passwd2:
                    return -2,"两次密码不同，修改失败"
                else:
                    return passwd1,"密码修改成功"

    #开户
    def createCard(self, idCard, name, phone, passwd1,money):
        bankSys = Bank()
        user = bankSys.usersDict.get(idCard)

        if not user:
            user = User(name, idCard, phone)
            # 存入系统
            bankSys.usersDict[idCard] = user
        cardId = self.getCardId()
        card = Card(cardId,passwd1,money)
        user.cardsDict[cardId] = card

        return "开卡成功！请牢记卡号：%s"%(cardId)


    #插卡
    def checkCard(self,cardId,passwd):
        # cardId = input("输入您的卡号：")
        #找到用户和用户的卡
        bankSys = Bank()
        print(bankSys.usersDict)
        # print(user.cardsDict)
        for idCard, user in bankSys.usersDict.items():
            for key, card in user.cardsDict.items():
                if key == cardId:
                    if card.passwd ==passwd:
                        return 1,"请稍后……",user, card
                    else:
                        return 0 ,"密码错误"
        return 0,"卡号不存在……"

    #查询
    def searchCard(self, card):
        if card.isLock:
            return -1,"该卡已被锁定，请解锁后继续其他操作！"
        else:
            return "卡号：%s    余额:%.2f"%(card.cardId, card.money)

    #存款
    def deposit(self, card,money):
        if card.isLock:
            return card.isLock,"该卡已被锁定，请解锁后继续其他操作！"
        else:
            self.money += money
            money1 = int(card.money)
            money1 += money
            card.money = money1
            return False,card.money

    #取款
    def withdrawal(self, card,money):
        if card.isLock:
            return card.isLock,"该卡已被锁定，请解锁后继续其他操作！"
        else:
            self.money -= money
            money1 = int(card.money)
            money1 -= money
            card.money = money1

            return False,"取款成功！！！"

    #解锁
    def unlock(self, user, card):
        if card.isLock:
            card.isLock = False
            return card.isLock,"解锁成功！"
        else:
            return False,"该卡未被锁定！"

    #修改密码
    def changepasswd(self,card):
        if card.isLock:
            print("该卡已被锁定，请解锁后继续其他操作！")
            if not self.inputPasswd(card.passwd):

                passwd1 = input("请输入新密码：")
                passwd2 = input("请输验证密码：")
                if passwd1 != passwd2:
                    print("两次密码不同，修改失败")
                else:
                    card.passwd = passwd1
                    print("系统密码修改成功")
                    return 0
            else:
                print("密码验证错误！！")

    #注销
    def logout(self,card):
        if card.isLock:
            return card.isLock,"该卡已被锁定，请解锁后继续其他操作！"
        else:
            # if not self.inputPasswd(card.passwd):
            bankSys = Bank()
            for idCard, user in bankSys.usersDict.items():
                for key, card1 in user.cardsDict.items():
                    if key == card.cardId:
                        del user.cardsDict[key]
                            # print("账户注销成功")
                        return False,"账户注销成功"


    #锁定
    def lock(self, user, card):
        if card.isLock:
            return card.isLock,"该卡已被锁定，请解锁后继续其他操作！"
        else:
            card.isLock = True
            return False,"锁定成功！"

    #转账
    def transfer(self, card,cardId1,money):
        if card.isLock:
            return card.isLock,"该卡已被锁定，请解锁后继续其他操作！"
        else:
            bankSys = Bank()
            for idCard, user in bankSys.usersDict.items():
                for key, card1 in user.cardsDict.items():
                    if key == cardId1:
                        card.money = float(card.money)
                        money1 = float(card1.money)
                        money = float(money)
                        money1 += money
                        if money > card.money:
                            return 0,"卡内余额不足……"
                        else:
                            card.money -= money
                            card1.money = money1
                            print("转账成功！！")
                            return 1,"转账成功！！"
            return 2,"输入账号不存在！！"

    #补卡
    def reisse(self, idCard, cardid, passwd1):
        bankSys = Bank()
        for idCard1, user in bankSys.usersDict.items():
            if idCard == idCard1:
                if cardid in user.cardsDict:
                    money = user.cardsDict[cardid].money
                    cardId = self.getCardId()
                    card = Card(cardId, passwd1, money)
                    user.cardsDict[cardId] = card
                    del user.cardsDict[cardid]
                    return "补卡成功！请牢记卡号：%s" % (cardId)
                else:
                    return "您的名下没有此卡"
        return "您还没有开户！！"
    #输入密码，并与真实密码进行比对，比对成功返回0，否则返回1
    def inputPasswd(self, realPasswd,passwd):
        for i in range(3):
            # passwd = input("请输入密码：")
            if passwd == realPasswd:
                #验证成功
                return 0
        return 1

    #随机获取一个卡号
    def getCardId(self):
        arr = "0123456789"
        cardId = ""
        for i in range(6):
            cardId += random.choice(arr)
        return cardId
