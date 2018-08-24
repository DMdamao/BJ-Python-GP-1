# -*- coding:utf-8 -*-
from bank import Bank
from user import User
from card import Card

import random

class ATM(object):
    def __init__(self):
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
        print("================================================")
        print("=     用户名:%s        卡号:%s  "%(name, cardId))
        print("=          查询(1)           转账(2)           ")
        print("=          存款(3)           取款(4)           ")
        print("=          改密(5)           注销(6)           ")
        print("=          锁定(7)           解锁(8)           ")
        print("=                   退卡(9)                    ")
        print("================================================")

    def checkPasswd(self,account,passwd):
        # account = input("请输入系统账号：")
        # passwd = input("请输入系统密码：")
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
        # money = int(input("请输入提额额度："))
        self.money += money
        return "提额成功！！"
        if not self.isActive:
            self.isActive = True

    def changeAtmPasswd(self,passwd, passwd1, passwd2):
        # passwd = input("请输入原始密码：")
        if passwd != self.passwd:
            return "密码错误，修改失败"
        else:
            # passwd1 = input("请输入新密码：")
            # passwd2 = input("请输验证密码：")
            if passwd1 != passwd2:
                return "两次密码不同，修改失败"
            else:
                self.passwd = passwd1
                return "系统密码修改成功"
    #开户
    def createCard(self):
        idCard = input("请输入您的身份证号：")
        #验证是否存在该用户
        bankSys = Bank()

        user = bankSys.usersDict.get(idCard)

        if not user:
            #用户不存在，需要创建用户
            name = input("请输入您的姓名：")
            phone = input("请输入您的手机号：")
            user = User(name, idCard, phone)
            # 存入系统

            bankSys.usersDict[idCard] = user


        #开卡
        #设置密码
        passwd1 = input("请设置密码：")
        #验证密码
        if self.inputPasswd(passwd1):
            print("三次密码验证错误，开卡失败")
            return
        money = float(input("输入预存款："))
        cardId = self.getCardId()
        card = Card(cardId,passwd1,money)
        user.cardsDict[cardId] = card

        print("开卡成功！请牢记卡号：%s"%(cardId))


    #插卡
    def checkCard(self):
        cardId = input("输入您的卡号：")
        #找到用户和用户的卡
        bankSys = Bank()
        for idCard, user in bankSys.usersDict.items():
            for key, card in user.cardsDict.items():
                if key == cardId:
                    #找到卡了，验证密码了
                    if self.inputPasswd(card.passwd):
                        card.isLock = True
                        print("三次密码错误，该卡被锁定！！")
                        return 0
                    print("请稍后……")
                    return user, card
        print("卡号不存在……")
        return 0

    #补卡
    def reisse(self):
        idCard = input("请输入身份证号：")
        bankSys = Bank()
        for idCard1, user in bankSys.usersDict.items():
            if idCard == idCard1:
                print("您的名下有%d张卡" % (len(user.cardsDict)))
                for key, card in user.cardsDict.items():
                    print("卡号为：%s"%(key))

                cardid = input("请输入要补办的卡号：")

                if cardid in user.cardsDict:

                    passwd1 = input("请设置密码：")
                    # 验证密码
                    if self.inputPasswd(passwd1):
                        print("三次密码验证错误，补卡失败")
                        return
                    money =user.cardsDict[cardid].money
                    cardId = self.getCardId()
                    card = Card(cardId, passwd1, money)
                    user.cardsDict[cardId] = card
                    print("补卡成功！请牢记卡号：%s" % (cardId))
                    del user.cardsDict[cardid]
                    return
                else:
                    print("您的名下没有此卡")
                    return


        print("您还没开户！！")



    #查询
    def searchCard(self, card):
        if card.isLock:
            print("该卡已被锁定，请解锁后继续其他操作！")
        else:
            print("卡号：%s    余额:%.2f"%(card.cardId, card.money))
    #存款
    def deposit(self, card):
        if card.isLock:
            print("该卡已被锁定，请解锁后继续其他操作！")
        else:
            money = float(input("输入存款金额："))
            self.money += money
            card.money += money
            print("存款成功！余额：%.2f"%card.money)
    #取款
    def withdrawal(self, card):
        if card.isLock:
            print("该卡已被锁定，请解锁后继续其他操作！")
        else:
            money = float(input("输入取款金额："))
            if money > card.money:
                print("卡内余额不足……")
            elif money > self.money:
                print("提款机余额不足……")
            else:
                self.money -= money
                card.money -= money
            print("取款成功！余额：%.2f" % card.money)

    #解锁
    def unlock(self, user, card):
        if not card.isLock:
            print("该卡未被锁定，无需解锁操作！")
        else:
            idCard = input("输入身份证号：")
            if idCard != user.idCard:
                print("身份证验证失败，解锁失败！！")
            else:
                card.isLock = False
                print("解锁成功，可以继续其他操作！")

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
            print("该卡已被锁定，请解锁后继续其他操作！")
        else:
            if not self.inputPasswd(card.passwd):
                bankSys = Bank()
                for idCard, user in bankSys.usersDict.items():
                    for key, card1 in user.cardsDict.items():
                        if key == card.cardId:
                            del user.cardsDict[key]
                            print("账户注销成功")
                            return 0
                print("您还没有开户！！！")

            else:
                print("密码验证错误！！")

    #锁定
    def lock(self, user, card):

            idCard = input("输入身份证号：")
            if idCard != user.idCard:
                print("身份证验证失败，锁定失败！！")
            else:
                card.isLock = True
                print("锁定成功！")

    #转账
    def transfer(self, card):
        if card.isLock:
            print("该卡已被锁定，请解锁后继续其他操作！")
        else:
            tran_cardid = input("请输入转入卡号：")
            bankSys = Bank()
            for idCard, user in bankSys.usersDict.items():
                for key, card1 in user.cardsDict.items():
                    if key == tran_cardid:
                        money = float(input("请输入转账金额："))
                        if not self.inputPasswd(card.passwd):
                            if money > card.money:
                                print("卡内余额不足……")
                            else:
                                card.money -= money
                                card1.money += money
                                print("转账成功！！")
                                return
            print("输入账号不存在！！")




    #输入密码，并与真实密码进行比对，比对成功返回0，否则返回1
    def inputPasswd(self, realPasswd):
        for i in range(3):
            passwd = input("请输入密码：")
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
