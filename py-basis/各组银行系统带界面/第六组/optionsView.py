import tkinter as tk
from  tkinter import Frame, Label, W, E, Button, LEFT, RIGHT, BOTH, YES, NO, TOP, Variable,messagebox
from singleton import singletonDeco
from atm import ATM
from bank import Bank
from user import User
from card import Card
from tkinter import *
import atmInitView

import math, sys, time, random, threading

atm = ATM()
bank = Bank()
'''松耦合'''
# 返回*********************************************************************************
class BackDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('是否返回')
        self.isback = 0
        # 弹窗界面

    def setup_UI(self):
        # 第一行（两列）
        self.geometry("300x150+800+400")

        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=20)
        Label(row1, text="是否返回初始界面？", font=("宋体", 15), width=30).pack(side=TOP)

        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=20)
        tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row3, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)
    def ok(self):
        self.destroy()
        self.isback = 1
    def cancel(self):
        self.destroy()

#倒计时********************************************************************************
class WaitCloseDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('正在退卡')

    def setup_UI(self):
        self.resizable(False, False)
        self.geometry("300x150+800+400")
        self.tip = tk.StringVar()

        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(anchor=tk.CENTER ,pady=5)
        Label(row1, textvariable=self.tip, font=("宋体", 15)).pack(anchor=tk.CENTER, pady=50)

        def autoClose():
            for i in range(2):
                self.tip.set("正在退卡，还有%ds..."%(1-i))
                time.sleep(1)
            try:
                self.destroy()
            except:
                pass
        t = threading.Thread(target=autoClose)
        t.start()

# 开户*********************************************************************************
class creatUserDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('开户窗口')
        # 弹窗界面
        self.setup_UI()
    def setup_UI(self):
        self.geometry("350x250+780+400")
        self.tip = tk.StringVar()
        self.name = tk.StringVar()

        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=5)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP, pady=5)
        tk.Label(row1, text='请输入您的姓名：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.name, width=20).pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=5)
        tk.Label(row2, text='请输入身份证号：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.IdCard = tk.StringVar()
        tk.Entry(row2, textvariable=self.IdCard, width=20).pack(side=tk.LEFT)

        # 第三行
        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=5)
        tk.Label(row3, text='请输入电话号码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.phone = tk.StringVar()
        tk.Entry(row3, textvariable=self.phone, width=20).pack(side=tk.LEFT)

        row4 = tk.Frame(self)
        row4.pack(side=TOP, pady=5)
        tk.Label(row4, text='请设置该卡密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.passwd = tk.StringVar()
        tk.Entry(row4, textvariable=self.passwd, width=20).pack(side=tk.LEFT)

        row5 = tk.Frame(self)
        row5.pack(side=TOP, pady=5)
        tk.Label(row5, text='请输入预存款数：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.money = tk.StringVar()
        tk.Entry(row5, textvariable=self.money, width=20).pack(side=tk.LEFT)

        # 第六行
        row6 = tk.Frame(self)
        row6.pack(side=TOP, pady=10)
        tk.Button(row6, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row6, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)
    # 随机生成卡号
    def randomCardId(self):
        cid = ""
        for i in range(4):
            cid += str(random.choice(range(10)))
        # print(cid, self.cardList)
        if cid in bank.usersDict:
            self.randomCardId()
        else:
            return cid
    # 检查身份证号
    def veridCard(self,idcard, name):
        for value in bank.usersDict.values():
            # print(value)
            if str(idcard) == str(value["idCard"]) and str(name)!= str(value["name"]) :
                return False
        return True

    def ok(self):
        # print(self.name.get())
        if self.name.get().strip() != "":
            if self.IdCard.get().strip() != "" and self.veridCard(self.IdCard.get(), self.name.get()):
                if self.phone.get().strip() != "":
                    if self.passwd.get().strip() != "":
                        if self.money.get().strip() != "":
                            try:
                                int(self.IdCard.get())
                                int(self.phone.get())
                                money = float(self.money.get())
                            except:
                                pass
                            self.cardId = self.randomCardId()
                            card = Card(self.cardId, self.passwd.get(), money)
                            user = User(self.name.get(), self.IdCard.get(), self.phone.get())
                            bank.usersDict[self.cardId] = {"name": user.name, "phone": user.phone,
                                                           "passwd": card.passwd, "money": card.money,
                                                           "money": card.money, "isLock": card.isLock,
                                                           "idCard":user.idCard}
                            print(bank.usersDict)
                            messagebox.askokcancel("开户成功","请牢记您的卡号：%s"%self.cardId)
                            self.destroy()
                        else:
                            self.tip.set("预存款不能为空！")
                    else:
                        self.tip.set("密码不能为空！")
                else:
                    self.tip.set("电话号码不能为空！")
            else:
                self.tip.set("身份证号不能为空或者重复！")
        else:
            self.tip.set("姓名不能为空！")

        self.name.set("")
        self.IdCard.set("")
        self.phone.set("")
        self.passwd.set("")
        self.money.set("")

    def cancel(self):
        self.destroy()

# 改密*********************************************************************************
class changePasswdDialog(tk.Toplevel):
    def __init__(self,cardId):
        super().__init__()
        self.title('改密窗口')
        self.cardId = cardId
        # 弹窗界面

    def setup_UI(self):
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()
        self.old_passwd = tk.StringVar()

        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=5)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP,pady=5)
        tk.Label(row1, text='请输入原密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.old_passwd, width=20, show="*").pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=5)
        tk.Label(row2, text='请输入新密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.new_passwd1 = tk.StringVar()
        tk.Entry(row2, textvariable=self.new_passwd1, width=20, show="*").pack(side=tk.LEFT)

        # 第三行
        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=5)
        tk.Label(row3, text='再次确认新密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.new_passwd2 = tk.StringVar()
        tk.Entry(row3, textvariable=self.new_passwd2, width=20, show="*").pack(side=tk.LEFT)

        # 第四行
        row4 = tk.Frame(self)
        row4.pack(side=TOP, pady=10)
        tk.Button(row4, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row4, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        # print(bank.usersDict[self.cardId]["passwd"],self.old_passwd.get())
        if self.old_passwd.get() != "":
            if bank.usersDict[self.cardId]["passwd"] != self.old_passwd.get():
                self.tip.set("原密码输入错误！")
            else:
                if self.new_passwd1.get() != "":
                    if self.new_passwd1.get() != self.new_passwd2.get():
                        self.tip.set("新密码两次输入不一致！")
                    else:
                        bank.usersDict[self.cardId]["passwd"] = self.new_passwd1.get()
                        messge = messagebox.askokcancel("消息框", "密码修改成功！请牢记新密码：%s" % bank.usersDict[self.cardId]["passwd"])
                        try:
                            self.wait_window(messge)
                        except:
                            pass
                        self.destroy()
                else:
                    self.tip.set("新密码不能为空！")

        else:
            self.tip.set("原密码不能为空！")

        self.old_passwd.set("")
        self.new_passwd1.set("")
        self.new_passwd2.set("")

    def cancel(self):
        self.destroy()

# 锁卡*********************************************************************************
class lockedCardDialog(tk.Toplevel):
    def __init__(self, cardId):
        super().__init__()
        self.title('锁卡窗口')
        self.cardId = cardId
        # 弹窗界面
        self.setup_UI()
    def setup_UI(self):
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()
        self.old_passwd = tk.StringVar()

        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=5)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP, pady=5)
        tk.Label(row1, text='请输入卡密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.old_passwd, width=20, show="*").pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=5)
        tk.Label(row2, text='请输入身份证号：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.new_passwd1 = tk.StringVar()
        tk.Entry(row2, textvariable=self.new_passwd1, width=20, show="*").pack(side=tk.LEFT)

        # 第四行
        row4 = tk.Frame(self)
        row4.pack(side=TOP, pady=10)
        tk.Button(row4, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row4, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        # print("锁卡---",bank.usersDict[self.cardId]["passwd"], self.old_passwd.get())
        if self.old_passwd.get() != "":
            if bank.usersDict[self.cardId]["passwd"] != self.old_passwd.get():
                self.tip.set("原密码输入错误！")
            else:
                if bank.usersDict[self.cardId]["idCard"] != self.new_passwd1.get():
                    self.tip.set("身份证号错误！")
                else:
                    bank.usersDict[self.cardId]["isLock"] = True
                    messagebox.askokcancel("消息提示","此卡已被锁定！")
                    self.destroy()

        self.old_passwd.set("")
        self.new_passwd1.set("")


    def cancel(self):
        self.destroy()

# 解锁*********************************************************************************
class unlockedCardDialog(tk.Toplevel):
    def __init__(self, cardId):
        super().__init__()
        self.title('解锁窗口')
        self.cardId = cardId
        # 弹窗界面
    def setup_UI(self):
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()
        self.old_passwd = tk.StringVar()

        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=5)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP, pady=5)
        tk.Label(row1, text='请输入卡密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.old_passwd, width=20, show="*").pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=5)
        tk.Label(row2, text='请输入身份证号：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.new_passwd1 = tk.StringVar()
        tk.Entry(row2, textvariable=self.new_passwd1, width=20, show="*").pack(side=tk.LEFT)

        # 第四行
        row4 = tk.Frame(self)
        row4.pack(side=TOP, pady=10)
        tk.Button(row4, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row4, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        # print("锁卡---",bank.usersDict[self.cardId]["passwd"], self.old_passwd.get())
        if self.old_passwd.get() != "":
            if bank.usersDict[self.cardId]["passwd"] != self.old_passwd.get():
                self.tip.set("原密码输入错误！")
            else:
                if bank.usersDict[self.cardId]["idCard"] != self.new_passwd1.get():
                    self.tip.set("身份证号错误！")
                else:
                    bank.usersDict[self.cardId]["isLock"] = False
                    messagebox.askokcancel("消息提示","此卡已被解锁！")
                    self.destroy()

        self.old_passwd.set("")
        self.new_passwd1.set("")

    def cancel(self):
        self.destroy()

# 补卡*********************************************************************************
class modCardIdDialog(tk.Toplevel):
    def __init__(self, cardId):
        super().__init__()
        self.title('解锁窗口')
        self.cardId = cardId
        # 弹窗界面
    def setup_UI(self):
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()
        self.old_passwd = tk.StringVar()

        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=5)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP, pady=5)
        tk.Label(row1, text='请输入卡密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.old_passwd, width=20, show="*").pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=5)
        tk.Label(row2, text='请输入身份证号：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.new_passwd1 = tk.StringVar()
        tk.Entry(row2, textvariable=self.new_passwd1, width=20, show="*").pack(side=tk.LEFT)

        # 第四行
        row4 = tk.Frame(self)
        row4.pack(side=TOP, pady=10)
        tk.Button(row4, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row4, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    # 随机生成卡号
    def randomCardId(self):
        cid = ""
        for i in range(4):
            cid += str(random.choice(range(10)))
        # print(cid, self.cardList)
        if cid in bank.usersDict:
            self.randomCardId()
        else:
            return cid

    def ok(self):
        # print("锁卡---",bank.usersDict[self.cardId]["passwd"], self.old_passwd.get())
        if self.old_passwd.get() != "":
            if bank.usersDict[self.cardId]["passwd"] != self.old_passwd.get():
                self.tip.set("原密码输入错误！")
            else:
                if bank.usersDict[self.cardId]["idCard"] != self.new_passwd1.get():
                    self.tip.set("身份证号错误！")
                else:
                    self.new_cardId = self.randomCardId()
                    bank.usersDict[self.new_cardId] = bank.usersDict.pop(self.cardId)
                    messagebox.askokcancel("消息提示","补卡成功！请牢记新卡号：%s"%self.new_cardId)
                    self.destroy()

        self.old_passwd.set("")
        self.new_passwd1.set("")

    def cancel(self):
        self.destroy()

# 插卡*********************************************************************************
class putinCardDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('插卡')
        # 弹窗界面
    def setup_UI(self):
        # 第一行（两列）
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()

        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=30)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP)
        tk.Label(row1, text='请输入卡号：', font=("宋体", 10), width=15).pack(side=tk.LEFT, pady=5)
        self.cardId = tk.StringVar()
        tk.Entry(row1, textvariable=self.cardId, width=20).pack(side=tk.LEFT)

        # 第二行
        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=20)
        tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row3, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        # print(bank.usersDict["cardsDict"])
        if self.cardId.get() in bank.usersDict:
            messagebox.askokcancel("消息提示","欢迎进入凯哥私人银行！")
            self.destroy()
        else:
            self.tip.set("该卡号不存在！请输入正确的卡号")
            # messagebox.askokcancel("消息提示","该卡号不存在！请输入正确的卡号")
            self.cardId.set("")

    def cancel(self):
        self.destroy()

# 存款*********************************************************************************
class addAccountDialog(tk.Toplevel):
    def __init__(self,cardId):
        super().__init__()
        self.title('插卡')
        self.cardId = cardId
        # 弹窗界面
    def setup_UI(self):
        # 第一行（两列）
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()

        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=30)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP)
        tk.Label(row1, text='请输入存款额：', font=("宋体", 10), width=15).pack(side=tk.LEFT, pady=5)
        self.money = tk.StringVar()
        tk.Entry(row1, textvariable=self.money, width=20).pack(side=tk.LEFT)  # 第二行
        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=20)
        tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row3, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        try:
            money = float(self.money.get())
        except:
            self.tip.set("存款数额错误，请重新输入")
            self.money.set("")
            return
        if money >= 0:
            atm.money += money
            # print(bank.usersDict[self.cardId]["money"])
            bank.usersDict[self.cardId]["money"] += money
            # print(bank.usersDict[self.cardId]["money"])

            self.destroy()
        self.tip.set("存款数额错误，请重新输入")
        self.money.set("")

    def cancel(self):
        self.destroy()

# 取款*********************************************************************************
class getAccountDialog(tk.Toplevel):
    def __init__(self,cardId):
        super().__init__()
        self.title('插卡')
        self.cardId = cardId
        # 弹窗界面
    def setup_UI(self):
        # 第一行（两列）
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()

        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=10)
        Label(row1, textvariable=self.tip, font=("宋体", 11), width=35, pady=5).pack(side=TOP)
        tk.Label(row1, text='请输入取款额：', font=("宋体", 10), width=15).pack(side=tk.LEFT, pady=5)
        self.money = tk.StringVar()
        tk.Entry(row1, textvariable=self.money, width=25).pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=10)
        tk.Label(row2, text='请输入卡密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT, pady=5)
        self.passwd = tk.StringVar()
        tk.Entry(row2, textvariable=self.passwd, width=25, show="*").pack(side=tk.LEFT)

        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=20)
        tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row3, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        try:
            money = float(self.money.get())
            passwd = self.passwd.get()
        except:
            self.tip.set("存款数额错误，请重新输入")
            self.passwd.set("")
            self.money.set("")
            return
        if passwd != bank.usersDict[self.cardId]["passwd"]:
            self.tip.set("密码错误，请重新输入")
        else:
            if money >= 0 :
                if money <= bank.usersDict[self.cardId]["money"]:
                    if money <= atm.money:
                        atm.money -= money
                        # print(bank.usersDict[self.cardId]["money"])
                        bank.usersDict[self.cardId]["money"] -= money
                        # print(bank.usersDict[self.cardId]["money"])
                        self.destroy()
                    else:
                        self.tip.set("ATM机内余额不足！当前仅剩￥%.2f"%atm.money)
                else:
                    self.tip.set("卡内余额不足！")
            else:
                self.tip.set("取款额输入错误！")

        self.money.set("")
        self.passwd.set("")

    def cancel(self):
        self.destroy()

# 转账*********************************************************************************
class transAcountDialog(tk.Toplevel):
    def __init__(self,cardId):
        super().__init__()
        self.title('插卡')
        self.cardId = cardId
        # 弹窗界面
    def setup_UI(self):
        # 第一行（两列）
        self.geometry("350x200+800+400")
        self.tip = tk.StringVar()

        row = tk.Frame(self)
        row.pack(side=TOP, pady=5)
        Label(row, textvariable=self.tip, font=("宋体", 11), width=35, pady=2).pack(side=TOP)

        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=5)
        tk.Label(row1, text='请输入转账额：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.money = tk.StringVar()
        tk.Entry(row1, textvariable=self.money, width=25).pack(side=tk.LEFT)

        row4 = tk.Frame(self)
        row4.pack(side=TOP, pady=5)
        tk.Label(row4, text='请输对方卡号：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.out_cardId = tk.StringVar()
        tk.Entry(row4, textvariable=self.out_cardId, width=25).pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=5)
        tk.Label(row2, text='请输入卡密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.passwd = tk.StringVar()
        tk.Entry(row2, textvariable=self.passwd, width=25, show="*").pack(side=tk.LEFT)



        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=10)
        tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row3, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        try:
            money = float(self.money.get())
            passwd = self.passwd.get()
            out_cardId = self.out_cardId.get()
            # print("**********",bank.usersDict[out_cardId]["name"][1:])
        except:
            self.tip.set("存款数额错误，请重新输入")
            self.passwd.set("")
            self.money.set("")
            self.out_cardId.set("")
            return
        if out_cardId in bank.usersDict and out_cardId != self.cardId:
            if passwd != bank.usersDict[self.cardId]["passwd"]:
                self.tip.set("密码错误，请重新输入")
            else:
                if money >= 0 :
                    if money <= bank.usersDict[self.cardId]["money"]:
                        if money <= atm.money:
                            if messagebox.askokcancel("转账提示","请再次确认是否向\n  卡号：%s\n  姓名：*%s\n转账￥%.2f"%(out_cardId,
                                                        bank.usersDict[out_cardId]["name"][1:], bank.usersDict[out_cardId]["money"])):
                                atm.money -= money
                                # print(bank.usersDict[self.cardId]["money"])
                                bank.usersDict[self.cardId]["money"] -= money
                                # print(bank.usersDict[self.cardId]["money"])
                                self.destroy()
                            else:
                                self.tip.set("已取消转账操作")
                        else:
                            self.tip.set("ATM机内余额不足！当前仅剩￥%.2f"%atm.money)
                    else:
                        self.tip.set("卡内余额不足！")
                else:
                    self.tip.set("取款额输入错误！")
        else:
            self.tip.set("该卡号不存在，请输入正确卡号！")
        self.out_cardId.set("")
        self.money.set("")
        self.passwd.set("")

    def cancel(self):
        self.destroy()


# 主窗******************************************************************************************

class OptionsView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.insCardId = " "

    def setupOptionsView(self):
        # self.pack() # 若继承 tk.Frame ，此句必须有！
        self.title('管理员操作界面')
        self.geometry("900x600+500+230")
        # 程序参数/数据
        self.tipVar = Variable()
        # self.tipVar.set("当前ATM机内余额为：%.2f" % atm.cardId)
        self.resizable(width=False, height=False)
        # 使用Frame增加一层容器
        fm1 = Frame(self)
        fm2 = Frame(self)
        fm3 = Frame(self)
        fm4 = Frame(self)

        button_image_gif7 = PhotoImage(file="开户按钮.gif")
        Button(fm1, text='开户', font=("宋体", 15), image=button_image_gif7,  width=190, height=45,command=self.createUser).pack(side=TOP, anchor=W,expand=NO, pady =7)
        button_image_gif8 = PhotoImage(file="存款按钮.gif")
        Button(fm1, text='存款', font=("宋体", 15), image=button_image_gif8,  width=190, height=45,command=self.addAcount).pack(side=TOP, anchor=W,expand=NO, pady =7)
        button_image_gif9 = PhotoImage(file="改密按钮.gif")
        Button(fm1, text='改密', font=("宋体", 15), image=button_image_gif9,  width=190, height=45,command=self.modPasswd).pack(side=TOP, anchor=W,expand=NO, pady =7)
        button_image_gif10 = PhotoImage(file="锁定按钮.gif")
        Button(fm1, text='锁卡', font=("宋体", 15), image=button_image_gif10,  width=190, height=45,command=self.lockedCard).pack(side=TOP, anchor=W,expand=NO, pady =7)
        button_image_gif11 = PhotoImage(file="退卡按钮.gif")
        Button(fm1, text='退卡', font=("宋体", 15),image=button_image_gif11,  width=190, height=45,command=self.outPutCard).pack(side=TOP, anchor=W,expand=NO, pady =7)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES, pady=60)

        Label(fm3, text="SUNCK IS A GOOD MAN",
              font=("宋体", 15), width=30, height=7, wraplength=350).pack(side=TOP,padx= 20)
        Label(fm3, textvariable=self.tipVar, font=("宋体", 11), width=40, height=10).pack(side=TOP)
        button_image_gif12 = PhotoImage(file="退出按钮.gif")
        Button(fm4, text='退出', font=("宋体", 15), image=button_image_gif12, width=190, height=45,command=self.shutdown).pack(side=LEFT, anchor=tk.N,expand=NO, padx= 70)
        button_image_gif13 = PhotoImage(file="插卡按钮.gif")
        Button(fm4, text='插卡', font=("宋体", 15), image=button_image_gif13,  width=115, height=27,command=self.putinCard).pack(side=RIGHT, anchor=tk.S,expand=NO,padx= 50)
        fm4.pack(side=tk.BOTTOM,fill= "x", expand=YES)
        fm3.pack(side=LEFT, fill=BOTH, expand=YES)

        button_image_gif14 = PhotoImage(file="转账按钮.gif")
        Button(fm2, text='转账', font=("宋体", 15), image=button_image_gif14,  width=190, height=45,command=self.transAcount).pack(side=TOP, anchor=E,expand=NO, pady =7)
        button_image_gif15 = PhotoImage(file="取款按钮.gif")
        Button(fm2, text='取款', font=("宋体", 15), image=button_image_gif15,  width=190, height=45,command=self.getAcount).pack(side=TOP, anchor=E,expand=NO, pady =7)
        button_image_gif16 = PhotoImage(file="补卡按钮.gif")
        Button(fm2, text='补卡', font=("宋体", 15), image=button_image_gif16,  width=190, height=45,command=self.repairCard).pack(side=TOP, anchor=E,expand=NO, pady =7)
        button_image_gif17 = PhotoImage(file="解锁按钮.gif")
        Button(fm2, text='解锁', font=("宋体", 15), image=button_image_gif17,  width=190, height=45,command=self.unlockedCard).pack(side=TOP, anchor=E,expand=NO, pady =7)
        button_image_gif18 = PhotoImage(file="返回按钮.gif")
        Button(fm2, text='返回', font=("宋体", 15), image=button_image_gif18,  width=190, height=45,command=self.back).pack(side=TOP, anchor=E,expand=NO, pady =3)

        fm2.pack(side=RIGHT, fill=BOTH, expand=YES, pady=60)
        self.mainloop()

    # 开户
    def createUser(self):
        creatUserDialog()

    # 插卡
    def putinCard(self):
        if self.isInCard():
            messagebox.askokcancel("消息提示", "当前有卡，请退卡后进行操作！")
        else:
            res = self.backputinCard()
            # print(res)
            if res !="":
                self.insCardId = res
                self.tipVar.set("当前卡号：%s    卡内余额：%.2f" % (self.insCardId, bank.usersDict[self.insCardId]["money"]))

    def backputinCard(self):
        picd = putinCardDialog()
        picd.setup_UI()
        self.wait_window(picd)
        return picd.cardId.get()

    # 改密
    def modPasswd(self):
        if self.isLocked():
            chPwdDlog = changePasswdDialog(self.insCardId)
            chPwdDlog.setup_UI()
            self.wait_window(chPwdDlog)

    # 锁卡
    def lockedCard(self):
        if self.isLocked():
            # print("islocked")
            lockedCardDialog(self.insCardId)

    # 解锁
    def unlockedCard(self):
        if self.isInCard():
            print(bank.usersDict[self.insCardId]["isLock"])
            if bank.usersDict[self.insCardId]["isLock"]:
                unlock = unlockedCardDialog(self.insCardId)
                unlock.setup_UI()
                self.wait_window(unlock)
            else:
                messagebox.askokcancel("消息提示", "此卡无需解锁,请勿重复解锁！")
        else:
            messagebox.askokcancel("消息提示","当前无卡，请插卡后进行操作！")

    # 存款
    def addAcount(self):
        if self.isLocked():
            addialog = addAccountDialog(self.insCardId)
            addialog.setup_UI()
            self.wait_window(addialog)
            # print("back",bank.usersDict[self.insCardId]["money"])
            self.tipVar.set("当前卡号：%s    卡内余额：%.2f" % (self.insCardId, bank.usersDict[self.insCardId]["money"]))

    # 取款
    def getAcount(self):
        if self.isLocked():
            getdialog = getAccountDialog(self.insCardId)
            getdialog.setup_UI()
            self.wait_window(getdialog)
            # print("back", bank.usersDict[self.insCardId]["money"])
            self.tipVar.set("当前卡号：%s    卡内余额：%.2f" % (self.insCardId, bank.usersDict[self.insCardId]["money"]))

    # 转账
    def transAcount(self):
        if self.isLocked():
            transdialog = transAcountDialog(self.insCardId)
            transdialog.setup_UI()
            self.wait_window(transdialog)
            # print("back", bank.usersDict[self.insCardId]["money"])
            self.tipVar.set("当前卡号：%s    卡内余额：%.2f" % (self.insCardId, bank.usersDict[self.insCardId]["money"]))

    # 返回
    def back(self):
        res = self.backView()
        # print("========", res)
        if res:
            self.quit()
            self.destroy()
            atmView = atmInitView.ATMInitView()
            atmView.setupATMInitView()

    def backView(self):
        if self.isInCard():
            waitcloseDialog = WaitCloseDialog()
            waitcloseDialog.setup_UI()
            self.wait_window(waitcloseDialog)
            return True
        else:
            backDlog = BackDialog()
            backDlog.setup_UI()
            self.wait_window(backDlog)
            return backDlog.isback
    # 补卡
    def repairCard(self):
        if self.isLocked():
            self.insCardId = self.backRepairCard()
            self.tipVar.set("当前卡号：%s    卡内余额：%.2f" % (self.insCardId, bank.usersDict[self.insCardId]["money"]))

    def backRepairCard(self):
        modCardIdDlog = modCardIdDialog(self.insCardId)
        modCardIdDlog.setup_UI()
        self.wait_window(modCardIdDlog)
        return modCardIdDlog.new_cardId

    # 退卡
    def outPutCard(self):
        if self.isInCard():
            self.insCardId = ""
            messagebox.askokcancel("消息提示","退卡成功！")
            self.tipVar.set("")
        else:
            # print("0000000000000000")
            messagebox.askokcancel("消息提示", "当前无卡，请插卡后进行操作！")

    # 退出
    def shutdown(self):
        sys.exit(0)

    # 检查是否插卡
    def isInCard(self):
        # print("**********",self.insCardId)
        if self.insCardId == " ":
            pass
        else:
            if self.insCardId in bank.usersDict:
                self.tipVar.set("当前卡号：%s    卡内余额：%.2f"%(self.insCardId, bank.usersDict[self.insCardId]["money"]))
                return True
        self.tipVar.set("")
        return False

    # 检查是否锁卡
    def isLocked(self):
        if self.isInCard():
                if bank.usersDict[self.insCardId]["isLock"]:
                    messagebox.askokcancel("消息提示","卡已被锁，请解锁后操作")
                    return False
                else:
                    return True
        else:
            messagebox.askokcancel("消息提示", "当前无卡，请插卡后进行操作！")

# OpView = OptionsView()
# OpView.setupOptionsView()
