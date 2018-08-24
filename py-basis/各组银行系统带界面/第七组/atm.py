# -*- coding:utf-8 -*-
from bank import Bank
from user import User
from card import Card
from atminitview import View
import random
a = View()
class ATM(object):
    def __init__(self):
        self.account = "1"
        self.passwd = "1"
        self.money = 0
        self.isActive = True

    # 登陆
    def checkPasswd(self):
        account = a.cardid('请输入账号')
        passwd = a.cardid('请输入密码')
        if account != self.account or passwd != self.passwd:
            a.error("密码或账号错误登陆失败")
            return 1
        else:
            a.error("系统设置成功，正在启动……")
            return 0

    # 提额
    def addMoney(self):
        money = int(a.cardid('请输入要提额度'))
        self.money += money
        a.error("提额成功现在额度为%d" % self.money)
        if not self.isActive:
            self.isActive = True

    # 改密
    def changeAtmPasswd(self):
        passwd = a.cardid('请输入原密码')
        if passwd != self.passwd:
            a.error("密码错误，修改失败")
        else:
            passwd1 = a.cardid('请输入新密码')
            passwd2 = a.cardid('请再次输入密码')
            if passwd1 != passwd2:
                a.error("两次密码不同，修改失败")
            else:
                self.passwd = passwd1
                a.error("系统密码修改成功")

    # 开户
    def createCard(self):
        idCard = a.cardid('请输您的身份证号')
        #验证是否存在该用户
        bankSys = Bank()
        user = bankSys.usersDict.get(idCard)
        if not user:
            #用户不存在，需要创建用户
            name = a.cardid('请输入姓名')
            phone = a.cardid('请输入手机号')
            user = User(name, idCard, phone)
            # 存入系统
            bankSys.usersDict[idCard] = user
        # 开卡
        # 设置密码
        passwd1 = a.cardid('请设置密码')
        # 验证密码
        if self.inputPasswd(passwd1):
            a.error("三次密码验证错误，开卡失败")
            return
        money = float(a.cardid('请输入预存款金额'))
        cardId = self.getCardId()
        card = Card(cardId, passwd1, money)
        user.cardsDict[cardId] = card
        a.error("开卡成功！请牢记卡号：%s" % (cardId))

    # 插卡
    def checkCard(self):
        cardId = a.cardid("输入您的卡号：")
        #找到用户和用户的卡
        bankSys = Bank()
        for idCard, user in bankSys.usersDict.items():
            for key, card in user.cardsDict.items():
                if key == cardId:
                    #找到卡了，验证密码了
                    if self.inputPasswd(card.passwd):
                        card.isLock = True
                        a.error("三次密码错误，该卡被锁定！！")
                        return 0
                    a.error("请稍后……")
                    return user, card
        a.error("卡号不存在……")
        return 0

    # 补卡
    def new_card(self):
        card3 = a.cardid("输入您的卡号：")
        # 找到用户和用户的卡
        bankSys = Bank()
        for idCard, user in bankSys.usersDict.items():
            for key, card in user.cardsDict.items():
                if key == card3:
                    if self.inputPasswd(card.passwd):
                        a.error("三次密码错误，补卡失败！！")
                        return 0
                    else:
                        money = card.money
                        cardId = self.getCardId()
                        card = Card(cardId, card.passwd, money)
                        del user.cardsDict[card3]
                        user.cardsDict[cardId] = card
                        a.error("补卡成功，新卡号为%s" % cardId)
                        return 1
        a.error("卡号不存在……")
        return 0

    #查询
    def searchCard(self, card):
        if card.isLock:
            a.error("该卡已被锁定，请解锁后继续其他操作！")
        else:
            a.error("卡号：%s    余额:%.2f" % (card.cardId, card.money))

    # 转账
    def transfer_accounts(self, card):
        if card.isLock:
            a.error("该卡已被锁定，请解锁后继续其他操作！")
        else:
            orher_card = a.cardid("输入对方卡号：")
            bankSys = Bank()
            for idCard, user in bankSys.usersDict.items():
                for key, card1 in user.cardsDict.items():
                    if key == orher_card:
                        money = float(a.cardid("输入转账金额："))
                        if money > card.money:
                            a.error("卡内余额不足……")
                        else:
                            card1.money += money
                            card.money -= money
                            a.error("转账成功！余额：%.2f" % card.money)
                        return 0
            a.error("卡号不存在……")

    #存款
    def deposit(self, card):
        if card.isLock:
            a.error("该卡已被锁定，请解锁后继续其他操作！")
        else:
            money = float(a.cardid("输入存款金额："))
            self.money += money
            card.money += money
            a.error("存款成功！余额：%.2f" % card.money)

    #取款
    def withdrawal(self, card):
        if card.isLock:
            a.error("该卡已被锁定，请解锁后继续其他操作！")
        else:
            money = float(a.cardid("输入取款金额："))
            if money > card.money:
                a.error("卡内余额不足……")
            elif money > self.money:
                a.error("提款机余额不足……")
            else:
                self.money -= money
                card.money -= money
                a.error("取款成功！余额：%.2f" % card.money)

    # 改密码
    def change_password(self, card):
        if self.inputPasswd(card.passwd):
            card.isLock = True
            a.error("三次密码错误，该卡被锁定！！")
            return 0
        else:
            cardpasswd1 = a.cardid("请输入新密码：")
            cardpasswd2 = a.cardid("请输验证密码：")
            if cardpasswd1 != cardpasswd2:
                card.isLock = True
                a.error("两次密码不同，修改失败，该卡被锁定！！")
            else:
                card.passwd = cardpasswd1
                a.error("系统密码修改成功,请重新登陆")
                return 0

    # 注销
    def logout(self, user, card):
        if card.money > 0:
            a.error("请先将卡内余额%.2f,取出或转入其他卡中在进行注销操作。" % card.money)
        elif self.inputPasswd(card.passwd):
            card.isLock = True
            a.error("三次密码错误，该卡被锁定！！")
            return 0
        else:
            idCard = a.cardid("输入身份证号：")
            if idCard != user.idCard:
                a.error("身份证验证失败，解锁失败！！")
            else:
                del card.cardId
                a.error("已将此卡注销")
                return 0

    # 锁定
    def lock(self, user, card):
        if card.isLock:
            a.error("该已经被锁定，无需操作！")
        else:
            idCard = a.cardid("输入身份证号：")
            if idCard != user.idCard:
                a.error("身份证验证失败，锁定失败！！")
            else:
                card.isLock = True
                a.error("锁定成功！")

    #解锁
    def unlock(self, user, card):
        if not card.isLock:
            a.error("该卡未被锁定，无需解锁操作！")
        else:
            idCard = a.cardid("输入身份证号：")
            if idCard != user.idCard:
                a.error("身份证验证失败，解锁失败！！")
            else:
                card.isLock = False
                a.error("解锁成功，可以继续其他操作！")

    #输入密码，并与真实密码进行比对，比对成功返回0，否则返回1
    def inputPasswd(self, realPasswd):
        for i in range(3):
            passwd = a.cardid("请输入密码：")
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
#   程序运行起来 
