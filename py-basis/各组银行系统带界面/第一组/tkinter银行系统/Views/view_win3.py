# -*- coding:utf-8 -*-

import tkinter as tk
import tkinter.messagebox  # 这个是消息框，对话框的关键
from Control.atm import ATM

'''
 存款、取款通用页面
'''


class Input_money(tk.Toplevel):
    def __init__(self, parent, db, card):
        super().__init__()
        self.db = db
        self.card = card
        self.type = self.change_type(parent.type)
        self.title("操作")
        self.parent = parent  # 显式地保留父窗口
        self.money = tk.StringVar()  # 输入框输入的钱数

        self.photo = tkinter.PhotoImage(file="Views/Image/2.png")  # 图片路径
        self.photo1 = tk.PhotoImage(file="Views/Image/bg1.png")

        self.setupUI()  # 这一句写在最下面

    def change_type(self, type):
        if type == 1:
            type = "取款"
        elif type == 2:
            type = "存款"


    # 取款/存款
    def func1(self):
        res = ATM.Withdraw_money(1, self.db, self.card.card_id, int(self.money.get()), self.parent.type)
        if res == 1:
            self.parent.message1.set("操作成功")
            if self.parent.type == 1:
                money = int(self.parent.money.get()) - int(self.money.get())
            else:
                money = int(self.parent.money.get()) + int(self.money.get())
            self.parent.money.set(money)
        else:
            self.parent.message1.set(res)
        self.destroy()


    # 程序主页面
    def setupUI(self):
        imgLabel = tkinter.Label(self,
                                 image=self.photo, width=300, height=200, compound=tkinter.CENTER,
                                 )
        imgLabel.place(x=0, y=0)

        text_label = tk.Label(self, text="输入金额：", fg="white", font=("宋体", 11),
                              image=self.photo1, width=80, height=30, compound=tkinter.CENTER)
        # 金额输入框
        money_entry = tk.Entry(self, textvariable=self.money, width=20, bd=5)

        button1 = tk.Button(self, text="确认", command=self.func1,
                            image=self.photo1, width=140, height=30, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white", )  # 自身的颜色

        text_label.place(x=3, y=40)
        money_entry.place(x=110, y=45)
        button1.place(x=115, y=120)
